%define version 0.0
%define rel 1
%define snapshot 20100510
%define gitrel git%{snapshot}
%define release %mkrel 0.%{gitrel}.%{rel}

%define sversion %{version}%{gitrel}

Name: mobile-broadband-provider-info
Summary: Mobile broadband providers database
Group: System/Configuration/Other
Version: %{version}
License: Public Domain
URL: http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
Release: %{release}
Source0: %{name}-%{snapshot}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: libxml2-utils

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%prep
%setup -q -n %{name}-%{snapshot}

%build
autoreconf -fi
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
