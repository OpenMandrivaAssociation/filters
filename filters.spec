
%define name	filters
%define version	2.40
%define rel	1
%define release %mkrel %rel

Name: %name
Version: %version
Release: %release
Summary: A collection of text filters, including the Swedish Chef
License: GPL
Group: Toys
URL: http://kitenet.net/~joey/code/filters.html
# author distributes tarball only from debian pool
Source: http://ftp.debian.org/debian/pool/main/f/filters/%{name}_%{version}.tar.gz
BuildRequires: flex, byacc

%description
A collection of filters to do all sorts of strange things to text.
This includes such favorites as B1FF and the Swedish Chef, and a
wide range of others.

%prep
%setup -q -n %{name}

sed -r -i '/\s+g*cc/s,g*cc,\$(CC),' Makefile *.dir/makefile

%build
export CC="%__cc %optflags"
%make

%install
rm -rf %{buildroot}
make install PREFIX="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README
%attr(0755,root,root) %{_gamesbindir}/*
%{_mandir}/man6/*
