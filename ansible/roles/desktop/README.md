# Desktop

> The `kde_` variables are related to the `desktop_env` variable.

## Variables

|Variable|Required|Default|Description
|:--:|:--:|:--:|:--:|
|`gpu_vendor`|❌|-|Must be `intel` or `nvidia`
|`gpu_nvidia_proprietary`|❌|`true`|Installs the proprietary driver instead of [Nouveau](https://wiki.archlinux.org/title/Nouveau)
|`gpu_nvidia_dkms`|❌|`false`|Required for custom kernels, see [here](https://wiki.archlinux.org/title/NVIDIA#Custom_kernel)
|`desktop_env`|❌|-|Must be `kde` or `xfce`
|`kde_applications`|❌|-|Installs [all](https://archlinux.org/groups/x86_64/kde-applications/) available packages for KDE
|`kde_minimal`|❌|`true`|Installs only `dolphin`, `dolphin-plugins`, `konsole` and `yakuake` besides KDE
|`install_firefox`|❌|`true`|Installs Mozilla Firefox
