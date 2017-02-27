Name: igmpproxy
Version: 0.1
Release: 6git
License: GPL
Group: System/Servers
Summary: Simple mulitcast router for Linux that only uses the IGMP protocol

Source0: http://sourceforge.net/projects/igmpproxy/igmpproxy-%{version}.tar.gz
Source1: igmpproxy.service

BuildRequires: gcc autoconf automake

%description
igmpproxy is a simple multicast router for Linux that only uses the IGMP
protocol.

%prep
%setup -q

%build
./bootstrap
%configure
%make

%install
%makeinstall
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}/usr/src
install -D -m 755 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc AUTHORS README NEWS
%{_sbindir}/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_unitdir}/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Thu Sep 04 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.1-5
+ Revision: 0c11b14
- Register service during installation

