# Arch Linux Setup

- **UEFI mode**
- [x86_64](https://en.wikipedia.org/wiki/X86-64)-compatible machine
- min. 512 MiB RAM
- 4 GiB available disk space

## Variables

|Variable|Required|Default|Description
|:--:|:--:|:--:|:--:|
|`sys_install_device`|✅|-|Device on which Arch Linux is to be installed (must be `/dev/sdX` or `/dev/nvme0nX`)
|`sys_part_boot_size_in_mb`|✅|512|Size of the `/boot` partition, must be specified in **MiB**
|`sys_part_swap_size_in_gb`|✅|4|Size of the swap file, must be specified in **GB**
|`sys_part_root_size`|✅|`100%`|Size of the `/root` partition, `100%` left by default but can be anything (e.g. `880G`)
|`sys_user_name`|✅|-|Name of your user account
|`sys_user_password`|✅|-|Password for the `sys_user_name` account
|`sys_root_password`|❌|-|Optional different password for the `root` account, otherwise `sys_user_password`
|`sys_user_name_public_key`|❌|-|Optional your public key to let ansible manage the post installation
|`sys_luks_password`|❌|-|Password to encrypt the root partition (and thus the system). This password **must** be entered at every boot.
|`sys_timezone`|❌|`Europe/Amsterdam`|Set the system timezone
|`sys_vim_as_vi`|❌|`true`|Replaces `vi` with `vim` using a symlink
|`sys_sudo_without_password`|❌|`false`|Allows users in `wheel` group to execute any command as `root` without being asked for permissions
|`sys_language`|❌|`en_US.UTF8`|[Setting the system locale](https://wiki.archlinux.org/title/Locale#Setting_the_system_locale)
|`sys_keymap`|❌|`de-latin1`|Keyboard layout for root tty
|`sys_hostname`|❌|`inventory_hostname`|If desired, an explicit hostname can be entered here, otherwise the name of the ansible inventory
|`sys_static_ip`|❌|`127.0.0.1`|For a system with a permanent IP address, replace `127.0.1.1` with that permanent IP address
|`sys_vfio`|❌|`false`|Load vfio-pci early using `mkinitcoio`
|`sys_iommu`|❌|`false`|Enable `iommu` via GRUB kernel parameters
|`sys_docker`|❌|`false`|Install `docker`, `docker-compose` and enable `docker.service` on system boot
|`pacman_parallel_downloads`|❌|`true`|Enables parallel downloads (5) via pacman
|`pacman_color`|❌|`true`|Activates a colored output from pacman
