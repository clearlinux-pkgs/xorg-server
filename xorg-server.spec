#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xB6B1CEAE5103DB07 (mattst88@gmail.com)
#
Name     : xorg-server
Version  : 21.1.13
Release  : 534
URL      : https://www.x.org/releases/individual/xserver/xorg-server-21.1.13.tar.gz
Source0  : https://www.x.org/releases/individual/xserver/xorg-server-21.1.13.tar.gz
Source1  : https://www.x.org/releases/individual/xserver/xorg-server-21.1.13.tar.gz.sig
Source2  : B6B1CEAE5103DB07.pkey
Summary  : Modular X.Org X Server
Group    : Development/Tools
License  : MIT
Requires: xf86-input-libinput
Requires: xf86-video-amdgpu
Requires: xf86-video-ati
Requires: xf86-video-fbdev
Requires: xf86-video-nouveau
Requires: xf86-video-vesa
Requires: xwayland
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : gnupg
BuildRequires : graphviz
BuildRequires : libdmx-dev
BuildRequires : libgcrypt-dev
BuildRequires : libxshmfence-dev
BuildRequires : libxslt-bin
BuildRequires : nettle-dev
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libbsd-overlay)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(libxcvt)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xf86dgaproto)
BuildRequires : pkgconfig(xfont)
BuildRequires : pkgconfig(xfont2)
BuildRequires : pkgconfig(xkbcomp)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : xkbcomp-bin
BuildRequires : xmlto
BuildRequires : xtrans-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-add-default-keyboard-setup-for-xorg.patch

%description
This is a submodule to access linux framebuffer devices.
It is supported to work as helper module (like vgahw)
for the chipset drivers.  There are functions for
saving/restoring/setting video modes, set palette entries,
and a few more helper functions.  Some of them can be
hooked directly into ScrnInfoRec.

%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) B6B1CEAE5103DB07' gpg.status
%setup -q -n xorg-server-21.1.13
cd %{_builddir}/xorg-server-21.1.13
%patch -P 1 -p1
pushd ..
cp -a xorg-server-21.1.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713229837
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/xorg-server
cp %{_builddir}/xorg-server-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xorg-server/11d1ae389a1a78f7832586e4c2a0c3c7263b7475 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/Xwayland
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/X11/xorg.conf.d/
cp 00-keyboard.conf %{buildroot}/usr/share/defaults/etc/X11/xorg.conf.d/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name} --skip-path /usr/bin/Xorg

%files
%defattr(-,root,root,-)
