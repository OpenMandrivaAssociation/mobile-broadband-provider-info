Name: mobile-broadband-provider-info
Summary: Mobile broadband providers database
Group: System/Configuration/Other
Version: 20110218
Release: %mkrel 2
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
