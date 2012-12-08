Name: mobile-broadband-provider-info
Summary: Mobile broadband providers database
Group: System/Configuration/Other
Version: 20110511
Release: %mkrel 3
License: Public Domain
URL: http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
Source0: http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: libxml2-utils

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/*


%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 20110511-1mdv2011.0
+ Revision: 674332
- update to new version 20110511

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 20110218-2
+ Revision: 666474
- mass rebuild

* Fri Apr 01 2011 Funda Wang <fwang@mandriva.org> 20110218-1
+ Revision: 649606
- New version 20110218

* Sun Jul 18 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.0-0.git20100510.1mdv2011.0
+ Revision: 554831
- update to current public release

* Mon Jan 25 2010 Frederik Himpe <fhimpe@mandriva.org> 0.0-0.git20100125.1mdv2010.1
+ Revision: 496348
- Update to new git snapshot

* Fri Nov 06 2009 Caio Begotti <caio1982@mandriva.org> 0.0-0.git20091103.1mdv2010.1
+ Revision: 461929
- some upstream updates which seemed to worth a bump

* Wed Oct 28 2009 Olivier Blin <oblin@mandriva.com> 0.0-0.git20091024.1mdv2010.0
+ Revision: 459756
- buildrequires libxml2-utils (instead of libxml2) for xmllint
- build as noarch
- initial release (from Caio Begotti)
- Created package structure for mobile-broadband-provider-info.

