### Computer

> 记录下，使用win10系统过程中，遇到的问题和解决的方案。

#### 问题 1

> 笔记本睡眠后，固态莫名其妙掉盘，蓝屏。

- 电源 -> 电源选项 -> 更改计划设置 -> 更改高级电源设置 -> PCI Express -> 链接状态电源管理 -> 关闭

#### 问题 2

> 外接显示屏，过几分钟，自动睡眠，电源选项设置无效。

- win + R -> regedit -> 计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\238C9FA8-0AAD-41ED-83F4-97BE242C8F20\7bc4a2f9-d8fc-4469-b07b-33eb785aaca0 -> Attributes改为2 

