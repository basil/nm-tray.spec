Name:           nm-tray
Summary:        NetworkManager tray icon
Version:        0.5.1
Release:        1%{?dist}

License:        GPL-2.0-or-later
URL:            https://github.com/palinek/%{name}
Source:         https://github.com/palinek/%{name}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)

Requires:       NetworkManager

%description
nm-tray is a simple NetworkManager frontend that displays an information icon
in the system tray (similar to nm-applet). It is a pure Qt application that
interacts with NetworkManager via the KF5::NetworkManagerQt API, using plain
D-Bus communication.

%prep
%autosetup -p1

%build
%cmake -DNM_TRAY_XDG_AUTOSTART_DIR=%{_sysconfdir}/xdg/autostart
%cmake_build

%install
%cmake_install
desktop-file-edit --remove-not-show-in=KDE --remove-not-show-in=GNOME --add-only-show-in=LXQt %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.conf
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

%changelog
* Tue Dec 23 2025 Basil Crow <me@basilcrow.com> - 0.5.1-1
- Initial packaging
