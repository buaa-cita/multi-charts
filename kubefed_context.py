import yaml,subprocess,os,argparse

def kubeEnv():
    subprocess.call(["sed -i '/KUBECONFIG/ d' ~/.bashrc"], shell=True)

def readKubeconfig(kubeconfig):
    with open(kubeconfig) as conf:
        return yaml.load(conf)

def scp(src,dst):
    print "scp", src,dst
    subprocess.call(["scp %s %s"%(src, dst)],shell=True)

def retrieveKubeconfig(hosts):
    subprocess.call(["mkdir -p context"],shell=True)
    hs = hosts.split(",")
    for h in hs:
        tmp = h.split(":")
        if len(tmp) <=1:
            print "Error: hosts format must be like hangzhou:1.1.1.1,beijing:2.2.2.2"
            exit(1)
        scp("root@%s:/etc/kubernetes/kube.conf"%tmp[1], "%s/context/%s-%s-kube.conf"%(os.getcwd(),tmp[0],tmp[1]))

def merge():
    content = {
        "apiVersion":"v1",
        "kind": "Config",
        "current-context": "hangzhou",
        "clusters": [],
        "contexts": [],
        "preferences": {},
        "users": []
    }
    context = "context"

    for f in os.listdir(os.path.abspath(context)):
        kubefile = os.path.join(context, f)
        if os.path.isfile(kubefile):
            tmp = os.path.basename(kubefile).split("-")
            config = readKubeconfig(kubefile)

            ## append cluster
            cluster=config["clusters"][0]
            cluster["name"] = "kubernetes-%s"%tmp[0]
            content["clusters"].append(cluster)

            ## append user
            user = config["users"][0]
            user["name"] = "kubernetes-admin-%s"%tmp[0]
            content["users"].append(user)

            ## append contexts
            ctx = config["contexts"][0]
            ctx["context"]["cluster"] = cluster["name"]
            ctx["context"]["user"] = user["name"]
            ctx["name"] = tmp[0]
            content["contexts"].append(ctx)
            content["current-context"] = tmp[0]
    with open('config', 'w') as out:
        yaml.dump(content, out, default_flow_style=False)

def with_args():
    help = '''
    tools for merge multiple kubeconfig file.
    It will automatically scp the remote dest file to local and execute merge process.
        eg. python context.py -h hangzhou:10.33.21.1,beijing:120.10.4.1
    '''

    parser = argparse.ArgumentParser(help)
    parser.add_argument("-H", "--hosts",
                        help="hosts where kubeconfig reside. eg. hangzhou:10.33.21.1,beijing:120.10.4.1")
    return parser.parse_args()

if __name__ == "__main__":

    kubeEnv()

    arg = with_args()

    # 1. backup config
    if not os.path.isdir(os.path.expanduser("~/.kube")):
        os.mkdir(os.path.expanduser("~/.kube"))
    if not os.path.isfile(os.path.expanduser("~/.kube/config.bak")):
        os.rename(os.path.expanduser("~/.kube/config"),os.path.expanduser("~/.kube/config.bak"))

    # 2. retrieve kubeconfig
    print "Info: host, %s ."%arg.hosts
    retrieveKubeconfig(arg.hosts)

    # 3. merge config
    merge()

    # 4. store file to destination
    if os.path.isfile("config"):
        os.rename(os.path.expanduser("config"),os.path.expanduser("~/.kube/config"))
        print "Info: file %s successfully generated."%os.path.expanduser("~/.kube/config")
    else:
        print "Warning: file generate fail, context/config."

