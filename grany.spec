%define name grany
%define version 2.0.0
%define release  %mkrel 2
%define summary The cellular automaton simulator

Name: %{name}
Summary: %{summary}
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Physics
Source0: http://guillaume.cottenceau.free.fr/html/grany-resource/grany-%{version}.tar.bz2
Source1: %{name}-pngicons.tar.bz2
Patch0: grany-2.0.0-gcc34.patch.bz2
URL: http://guillaume.cottenceau.free.fr/html/grany.html
BuildRequires: libgtkmm-devel

%description
Grany is a cellular automaton simulator. With it you can conduct computerized
experiments on cellular environments with a full-featured GUI.

%prep
%setup -q
%setup -D -T -a1
%patch0 -p0
%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << "EOF" > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): needs=X11 section=Applications/Sciences/Physics\
  title="Grany" command="%{_bindir}/grany" icon="grany.png" longtitle="%{summary}"
EOF

# icons
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
cp icons/grany-icon-16x16.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cp icons/grany-icon-32x32.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cp icons/grany-icon-48x48.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README FAQ AUTHORS docs/BASICS docs/CUSTOMIZATION
%{_bindir}/*
%{_datadir}/%{name}
%{_menudir}/%{name}
%{_iconsdir}/*.png
%{_iconsdir}/*/*.png

