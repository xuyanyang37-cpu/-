# Dell / Delta D1600E 95HR5 Firmware Reverse Engineering

主项目：研究 Dell/Delta 1600W PSU（95HR5 / 095HR5A）官方 00.3D.67 固件，重点分析 dsPIC33 系列控制器、PMBus/I²C、VOUT/OCP/OVP 与保护逻辑。

> 本仓库用于静态逆向、协议研究和硬件验证记录。默认不对电源执行任何写入或刷写操作。

## 当前固件

- Dell DUP：`VRTX_Power_Firmware_D1V85_LN_00.3D.67.BIN`
- DUP 大小：2,125,376 bytes
- DUP SHA-256：`5754a7740407e2357b914d9d1d74ec97d66e2cc158747a043e1b0114edd0d76e`
- 内嵌 payload：`095HR5_190AD_00.3D.67.bin`
- payload 大小：86,340 bytes
- 版本：`00.3D.67`
- PSU：Delta 1600W，PN 95HR5

## 已确认

2 MB 文件是 Dell Linux DUP，而不是直接的 dsPIC ROM。DUP 内含 `payload/095HR5_190AD_00.3D.67.bin`。

当前静态特征显示 payload 的 `0x104` 起存在连续 4-byte records：

```
00 xx xx xx
00 xx xx xx
00 xx xx xx
```

其余 3 bytes 具有 24-bit dsPIC/PIC24 instruction word 的外观，已生成 packed-24 分析副本，最终以 Ghidra dsPIC33E 解码结果为准。

## 逆向目标

- 中断向量与启动流程
- I²C/PMBus 命令分发
- READ_VOUT / VOUT_COMMAND
- OCP / OVP / UVP
- ADC / PWM / 数字电源控制环
- fault latch / thermal / fan
- EEPROM / 配置区
- C-like pseudocode

## 安全原则

不修改原始 BIN；不向实机写入未经验证的 PMBus 参数；补丁研究只针对副本。
