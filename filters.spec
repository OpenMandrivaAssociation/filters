%define name	filters
%define debug_package %{nil}

Name: %name
Version: 2.48
Release: 1
Summary: A collection of text filters, including the Swedish Chef
License: GPL
Group: Toys
URL: http://kitenet.net/~joey/code/filters.html
# author distributes tarball only from debian pool
Source: http://ftp.debian.org/debian/pool/main/f/filters/filters_2.48.tar.gz
BuildRequires: flex, byacc

%description
A collection of filters to do all sorts of strange things to text.
This includes such favorites as B1FF and the Swedish Chef, and a
wide range of others.

%prep
%setup -q -n %{name}

sed -r -i '/\s+g*cc/s,g*cc,\$(CC),' *.dir/makefile

%build
export CC="%__cc %optflags"
%make

%install
%makeinstall_std

%files
%defattr(0644,root,root,0755)
%doc README
%attr(0755,root,root) %{_gamesbindir}/*
%{_mandir}/man6/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.46-2mdv2011.0
+ Revision: 618285
- the mass rebuild of 2010.0 packages

* Thu Jul 09 2009 Anssi Hannula <anssi@mandriva.org> 2.46-1mdv2010.0
+ Revision: 393974
- new version
- fix format-security errors (printf-format.patch)

* Sun May 11 2008 Anssi Hannula <anssi@mandriva.org> 2.44-1mdv2009.0
+ Revision: 205453
- update to new version 2.44

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.40-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Anssi Hannula <anssi@mandriva.org> 2.40-1mdv2008.0
+ Revision: 77430
- 2.40
- Import filters



* Sat Jul 15 2006 Anssi Hannula <anssi@mandriva.org> 2.39-1mdv2007.0
- clean spec
- add URL
- apply %%optflags

* Wed Jun  1 2005 Claudio Matsuoka <claudio@mandriva.com> 2.33-1mdk
- created mdk package.

* Thu Aug 21 2003 Claudio Matsuoka <claudio@conectiva.com>
+ 2003-08-21 19:05:26 (34521)
- Initial commit.

