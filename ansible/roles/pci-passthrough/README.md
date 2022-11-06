# PCI Passthrough

Isolate PCI devices to pass them to a virtual machine

## Variables

|Variable|Required|Default|Description
|:--:|:--:|:--:|:--:|
|`pci_devices_to_isolate`|✅|-|Must be a list of PCI device names
|`kvm_no_reboot`|❌|`false`|Can be set to `true` to **not** reboot the system

## Isolating devices

1. Query the list of possible IOMMU groups: `iommu groups`

```text
❯ iommu groups
IOMMU Group 0:
	00:00.0 Host bridge [0600]: Intel Corporation Comet Lake-S 6c Host Bridge/DRAM Controller [8086:9b33] (rev 05)
IOMMU Group 1:
	00:01.0 PCI bridge [0604]: Intel Corporation 6th-10th Gen Core Processor PCIe Controller (x16) [8086:1901] (rev 05)
	01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GA104 [GeForce RTX 3070] [10de:2484] (rev a1)
	01:00.1 Audio device [0403]: NVIDIA Corporation GA104 High Definition Audio Controller [10de:228b] (rev a1)
IOMMU Group 2:
	00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [8086:1911]
IOMMU Group 3:
	00:12.0 Signal processing controller [1180]: Intel Corporation Comet Lake PCH Thermal Controller [8086:06f9]
IOMMU Group 4:
	00:14.0 USB controller [0c03]: Intel Corporation Comet Lake USB 3.1 xHCI Host Controller [8086:06ed]
	00:14.2 RAM memory [0500]: Intel Corporation Comet Lake PCH Shared SRAM [8086:06ef]
IOMMU Group 5:
	00:16.0 Communication controller [0780]: Intel Corporation Comet Lake HECI Controller [8086:06e0]
IOMMU Group 6:
	00:17.0 SATA controller [0106]: Intel Corporation Comet Lake SATA AHCI Controller [8086:06d2]
IOMMU Group 7:
	00:1b.0 PCI bridge [0604]: Intel Corporation Comet Lake PCI Express Root Port #17 [8086:06c0] (rev f0)
IOMMU Group 8:
	00:1b.4 PCI bridge [0604]: Intel Corporation Comet Lake PCI Express Root Port #21 [8086:06ac] (rev f0)
IOMMU Group 9:
	00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:06b8] (rev f0)
IOMMU Group 10:
	00:1c.6 PCI bridge [0604]: Intel Corporation Device [8086:06be] (rev f0)
IOMMU Group 11:
	00:1c.7 PCI bridge [0604]: Intel Corporation Device [8086:06bf] (rev f0)
IOMMU Group 12:
	00:1d.0 PCI bridge [0604]: Intel Corporation Comet Lake PCI Express Root Port #9 [8086:06b0] (rev f0)
IOMMU Group 13:
	00:1f.0 ISA bridge [0601]: Intel Corporation Z490 Chipset LPC/eSPI Controller [8086:0685]
	00:1f.3 Audio device [0403]: Intel Corporation Comet Lake PCH cAVS [8086:06c8]
	00:1f.4 SMBus [0c05]: Intel Corporation Comet Lake PCH SMBus Controller [8086:06a3]
	00:1f.5 Serial bus controller [0c80]: Intel Corporation Comet Lake PCH SPI Controller [8086:06a4]
	00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (7) I219-V [8086:15bc]
IOMMU Group 14:
	03:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP107 [GeForce GTX 1050 Ti] [10de:1c82] (rev a1)
	03:00.1 Audio device [0403]: NVIDIA Corporation GP107GL High Definition Audio Controller [10de:0fb9] (rev a1)
IOMMU Group 15:
	04:00.0 USB controller [0c03]: ASMedia Technology Inc. Device [1b21:3241]
IOMMU Group 16:
	05:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller [10ec:8125] (rev 04)
IOMMU Group 17:
	06:00.0 USB controller [0c03]: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller [1106:3483] (rev 01)
IOMMU Group 18:
	07:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]
```

2. Store the names of the desired devices in `pci_devices_to_isolate`:

```yaml
pci_devices_to_isolate:
  - RTX 3070
  - GA104 High Definition Audio Controller
  - VL805/806
```

3. Execute the playbook
