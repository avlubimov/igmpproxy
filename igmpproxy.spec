Name: igmpproxy
Version: 0.1
Release: 12git
License: GPL
Group: System/Servers
Summary: Simple mulitcast router for Linux that only uses the IGMP protocol

Source0: http://sourceforge.net/projects/igmpproxy/igmpproxy-%{version}.tar.gz

Requires:   rpcbind
BuildRequires: gcc autoconf automake

%description
igmpproxy is a simple multicast router for Linux that only uses the IGMP
protocol.

%prep
%setup -q

%build
./bootstrap
%configure
make

%install
%makeinstall
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}/usr/src
install -D -m 755 igmpproxy.service %{buildroot}/usr/lib/systemd/system/%{name}.service

%post
systemctl  daemon-reload 

%preun
systemctl stop  %{name}.service

%postun
systemctl  daemon-reload 


%files
%doc  README NEWS
%{_sbindir}/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
/usr/lib/systemd/system/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-12git
- fix spec (avlubimov@gmail.com)

* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-11git
- fix spec (avlubimov@gmail.com)

* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-10git
- fix spec (avlubimov@gmail.com)

* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-9git
- fix spec (avlubimov@gmail.com)

* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-8git
- fix spec (avlubimov@gmail.com)

* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-7git
- fix spec (avlubimov@gmail.com)

* Mon Feb 27 2017 avl <avlubimov@gmail.com> 0.1-6git
- init rpm package 
* Thu Sep 04 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.1-5
+ Revision: 0c11b14
- Register service during installation

