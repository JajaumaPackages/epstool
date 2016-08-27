Name:		epstool
Version:	3.08
Release:	9%{?dist}
Summary:	A utility to create or extract preview images in EPS files
Group:		Applications/Multimedia
License:	GPLv2+
URL:		http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm
Source0:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/ghostgum/%{name}-%{version}.tar.gz
# Patch to compile with gcc 4.3 and newer (taken from Gentoo)
Patch0:		epstool-3.08-gcc43.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Epstool is a utility to create or extract preview images in EPS files,
fix bounding boxes and convert to bitmaps.

Features:
* Add EPSI, DOS EPS or Mac PICT previews.
* Extract PostScript from DOS EPS files.
* Uses Ghostscript to create preview bitmaps.
* Create a TIFF, WMF, PICT or Interchange preview from part of a
  bitmap created by Ghostscript.
* works under Win32, Win64, OS/2 and Unix.
* works on little-endian machines (Intel) or big endian (Sun Sparc,
  Motorola) machines.

%prep
%setup -q
%patch0 -p1

%build
# SMP build doesn't work.
make

%install
rm -rf %{buildroot}
install -D -p -m 755 bin/epstool %{buildroot}%{_bindir}/epstool
install -D -p -m 644 doc/epstool.1 %{buildroot}%{_mandir}/man1/epstool.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENCE doc/epstool.htm doc/gsview.css
%{_bindir}/epstool
%{_mandir}/man1/epstool.1.*

%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.08-2
- Disable SMP build.

* Mon Jan 09 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.08-1
- First release.
