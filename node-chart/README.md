# node-chart

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 6.0.0](https://img.shields.io/badge/AppVersion-6.0.0-informational?style=flat-square)

**Used to initialize nodes and set related properties**

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Rivtower Technologies | contact@rivtower.com |  |
| BUAA | contact@buaa.edu.cn |  |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| node_name | string | `""` | Name of node |
| chain_name | string | `""` | The chain that contains the node |
| log_level | string | `"info"` | - |
| network_key | string | `""` | Private key used for communication encryption |
| node_address | string | `""` | Public key of node |
| node_key | string | `""` | Private key of node |
| kms_pwd | string | `"123456"` | Password for kms service |
| update_policy | string | `"AutoUpdate"` | - |
| node_port | string | `"40000"` | Port used to expose executor |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.4.0](https://github.com/norwoodj/helm-docs/releases/v1.4.0)

