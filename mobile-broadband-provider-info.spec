Name: mobile-broadband-provider-info
Summary: Mobile broadband providers database
Group: System/Configuration/Other
Version: 20120614
Release: 1
License: Public Domain
URL: http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
Source0: http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: libxml2-utils

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package devel
Summary: The pkgconfig for %{name}
Group: Development/GNOME and GTK+
Requires: %{name} = %{version}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files 
%{_datadir}/%{name}/*

%files devel
%{_datadir}/pkgconfig/%{name}.pc
