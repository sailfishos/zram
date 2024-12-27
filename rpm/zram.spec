Name:     zram
Version:  1.0.0
Release:  1
Summary:  ZRAM for swap config and services for Sailfish OS
License:  GPLv2+
Source0:  %{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: pkgconfig(libsystemd)
Requires: gawk
Requires: grep
Requires: util-linux

%description
ZRAM is a Linux block device that can be used for compressed swap in memory.
It's useful in memory constrained devices. This provides a service to setup
ZRAM as a swap device based on criteria such as available memory.

%prep
%autosetup

%build
# None required

%install
install -d %{buildroot}%{_sysconfdir}/
install -pm 0644 zram.conf %{buildroot}%{_sysconfdir}/

install -d %{buildroot}%{_unitdir}/swap.target.wants/
install -pm 0644 zram-swap.service %{buildroot}%{_unitdir}/
ln -s ../zram-swap.service %{buildroot}%{_unitdir}/swap.target.wants/

install -d %{buildroot}%{_sbindir}
install -pm 0755 zramstart %{buildroot}%{_sbindir}
install -pm 0755 zramstop %{buildroot}%{_sbindir}

%files
%license COPYING
%{_sysconfdir}/%{name}.conf
%{_unitdir}/*
%{_sbindir}/zramstart
%{_sbindir}/zramstop
