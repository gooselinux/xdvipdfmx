Summary: An extended version of DVIPDFMx with support for XeTeX output
Name: xdvipdfmx
Version: 0.4
Release: 5.1%{?dist}
License: GPLv2+
Group: Applications/Publishing
Source: http://scripts.sil.org/svn-view/xdvipdfmx/TAGS/xdvipdfmx-%{version}.tar.gz
URL: http://scripts.sil.org/xetex_linux

Requires: tex(tex), dvipdfmx
# dvipdfmx is required because some data files are shared
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# to build, we need various -devel packages...
BuildRequires: fontconfig-devel, freetype-devel, libpng-devel, zlib-devel, kpathsea-devel, libpaper-devel

%description
xdvipdfmx is an output driver for the XeTeX typesetting system.
It is an extended version of DVIPDFMx by Jin-Hwan Cho and Shunsaku Hirata,
which is itself an extended version of dvipdfm by Mark A. Wicks.
This driver converts XDV (extended DVI) output from the xetex program
into standard PDF that can be viewed or printed.

# # # # # # # # # #
# PREP
# # # # # # # # # #

%prep

# setup macro does standard clean-and-unpack
%setup -q

# # # # # # # # # #
# BUILD
# # # # # # # # # #

%build
chmod +x configure
%{configure} --with-freetype2=`freetype-config --prefix` 
make %{?_smp_mflags}

# # # # # # # # # #
# INSTALL
# # # # # # # # # #

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# # # # # # # # # #
# FILE LIST
# # # # # # # # # #

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/xdvipdfmx
%doc README AUTHORS BUGS COPYING TODO doc/tug2003.pdf index.html *.css

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4-5.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Neal Becker <ndbecker2@gmail.com> - 0.4-3
- Fix typo tex(tex)
- Add dist

* Thu Mar  6 2008 Neal Becker <ndbecker2@gmail.com> - 0.4-2
- Drop Vendor
- Add Req dvipdfmx
- Add doc
- Add BR libpaper-devel
- Drop Req fontconfig
- Req changed to tex(tex)

* Wed Mar  5 2008 Neal Becker <ndbecker2@gmail.com> - 0.4-1
- Update to 0.4


* Mon Mar  3 2008 Neal Becker <ndbecker2@gmail.com> - 0.3-1
- First try on Fedora

