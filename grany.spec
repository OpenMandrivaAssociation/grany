%define name grany
%define version 2.0.3
%define release 2
%define summary The cellular automaton simulator

Name: %{name}
Summary: %{summary}
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Physics
Source0: http://guillaume.cottenceau.free.fr/html/grany-resource/grany-%{version}.tar.bz2
Source1: %{name}-pngicons.tar.bz2
Source2:	.abf.yml
Patch2:	grany-2.0.3-gettext.patch
URL: https://guillaume.cottenceau.free.fr/html/grany.html
BuildRequires: pkgconfig(gtkmm-2.4)

%description
Grany is a cellular automaton simulator. With it you can conduct computerized
experiments on cellular environments with a full-featured GUI.

%prep
%setup -q
%setup -D -T -a1
%patch2 -p2 -b .datadir
%build
%configure2_5x
make

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Name=Grany
Exec=%{_bindir}/grany
Icon=grany
Comment=%{summary}
EOF

# icons
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
cp icons/grany-icon-16x16.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cp icons/grany-icon-32x32.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cp icons/grany-icon-48x48.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README FAQ AUTHORS docs/BASICS docs/CUSTOMIZATION
%{_bindir}/*
#%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/*.png
%{_iconsdir}/*/*.png



%changelog
* Thu Jan 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-2mdv2008.1
+ Revision: 142109
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import grany

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Jul 16 2004 Michael Scherer <misc@mandrake.org> 2.0.0-2mdk 
- rebuild for new gcc, patch 0

* Tue Apr  8 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.0-1mdk
- new release

* Wed Aug 21 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-4mdk
- rebuild for gcc 3.2

* Tue Jul 30 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-3mdk
- recompile against latest libstdc++

* Mon Jun 10 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.1-2mdk
- png icons (out xpm!)

* Tue May 14 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-1mdk
- new release that is friendly with g++-3.1

* Fri Feb 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-5mdk
- rebuild to fix invalid-packager

* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-4mdk
- fix obsolete-tag Copyright

* Tue Sep 11 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-3mdk
- rebuild

* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-2mdk
- rebuild

* Sun May  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-1mdk
- first build

