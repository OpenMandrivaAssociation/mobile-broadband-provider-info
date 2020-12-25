Summary:	Mobile broadband providers database
Name:		mobile-broadband-provider-info
Group:		System/Configuration/Other
Version:	20201225
Release:	1
License:	Public Domain
Url:		http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	libxml2-utils
BuildRequires:  xsltproc

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires: %{name} = %{EVRD}

%description devel
The pkgconfig for %{name}.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_datadir}/%{name}/*

%files devel
%{_datadir}/pkgconfig/%{name}.pc
