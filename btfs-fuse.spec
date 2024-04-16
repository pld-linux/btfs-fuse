Summary:	A bittorrent filesystem based on FUSE
Name:		btfs-fuse
Version:	2.24
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/johang/btfs/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ee01bbffbece1ea731f11868f9bd1916
URL:		https://github.com/johang/btfs/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.22.0
BuildRequires:	libfuse-devel >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtorrent-rasterbar-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	curl-libs >= 7.22.0
Requires:	libfuse >= 2.8.0
Requires:	libtorrent-rasterbar >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With BTFS, you can mount any .torrent file or magnet link and then use
it as any read-only directory in your file tree. The contents of the
files will be downloaded on-demand as they are read by applications.
Tools like ls, cat and cp works as expected. Applications like vlc and
mplayer can also work without changes.

%prep
%setup -q -n btfs-%{version}

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' scripts/btplay

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/btfs
%attr(755,root,root) %{_bindir}/btfsstat
%attr(755,root,root) %{_bindir}/btplay
%{_mandir}/man1/btfs.1*
