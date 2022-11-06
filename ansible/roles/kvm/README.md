# KVM

Installs `qemu`, `libvirt`, `swtpm` and `virt-manager`

## Variables

|Variable|Required|Default|Description
|:--:|:--:|:--:|:--:|
|`kvm_bar3_fix`|❌|-|Fix for BAR 3: `"cannot reserve [mem]" error in dmesg after starting virtual machine`
|`system_vfio`|❌|`false`|Load vfio-pci early using `mkinitcoio`
|`system_iommu`|❌|`false`|Enable `iommu` via GRUB kernel parameters
|`kvm_fix_permissions`|❌|`false`|Run `libvirtd.service` as `$USER`
|`tpm_fix_permissions`|❌|`false`|Run `swtpm` as `$USER`
|`kvm_no_reboot`|❌|`false`|Can be set to `true` to **not** reboot the system
