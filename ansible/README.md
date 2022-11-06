# ansible

A collection of custom `ansible` playbooks, for:

- UEFI based [Arch Linux](https://archlinux.org) installation
  - [LVM](https://wiki.archlinux.org/title/LVM) based root and swap partitions
  - Device encryption using [LUKS](https://wiki.archlinux.org/title/dm-crypt/Device_encryption)
  - Proper [localization](https://wiki.archlinux.org/title/Locale)
  - [Network configuration](https://wiki.archlinux.org/title/installation_guide#Network_configuration)
  - Configure root and personal user account with proper permissions
  - Enables parallel downloads and a colored output by default for `pacman`
  - Support for multiple kernels
  - `mkinitcpio` configuration with support for binding `vfio-pci` early
  - `intel_iommu` / `amd_iommu` can be automatically enabled during GRUB configuration
- Post installation (desktop)
  - Uses Xorg display manager
  - Support for Xfce and KDE (can be installed fully or minimal)
  - Support for LightDM and SDDM
  - Installs graphics driver (Intel/NVIDIA)
    - You can choose between proprietary and open source drivers
    - Installation of nvidia kernel modules can be automated using `dkms`
  - Installs Mozilla Firefox
- KVM
  - Supports binding `vfio-pci` early
  - Enables `intel_iommu` / `amd_iommu` (if desired and not yet active)
  - Optional fixes permissions for `libvirt` and `swtpm`
  - Can configure `mkinitcpio` to automatically isolate the PCI devices you want to pass through

## See also

1. System Setup
    - [Arch Linux](docs/system-setup/arch-linux.md)
2. [Desktop](roles/desktop/README.md)
3. [KVM](roles/kvm/README.md)
4. [PCI Passthrough](roles/pci-passthrough/README.md)
