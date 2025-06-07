#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeframever	5.116
%define		kf_ver		%{version}
%define		qt_ver		5.15.2
%define		kfname		plasma-framework

Summary:	The foundations that can be used to build a primary user interface
Summary(pl.UTF-8):	Podstawowe konstrukcje do zbudowania głównego interfejsu użytkownika
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	425fd39b0b689e60690feb514739d605
URL:		https://kde.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
%{?with_tests:BuildRequires:	Qt5Test-devel >= %{qt_ver}}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kactivities-devel >= %{kf_ver}
BuildRequires:	kf5-karchive-devel >= %{kf_ver}
%{?with_tests:BuildRequires:	kf5-kcompletion-devel >= %{kf_ver}}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf_ver}
BuildRequires:	kf5-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf5-kio-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf_ver}
%{?with_tests:BuildRequires:	kf5-kitemviews-devel >= %{kf_ver}}
%{?with_tests:BuildRequires:	kf5-kjobwidgets-devel >= %{kf_ver}}
BuildRequires:	kf5-knotifications-devel >= %{kf_ver}
BuildRequires:	kf5-kpackage-devel >= %{kf_ver}
BuildRequires:	kf5-kservice-devel >= %{kf_ver}
%{?with_tests:BuildRequires:	kf5-ktextwidgets-devel >= %{kf_ver}}
BuildRequires:	kf5-kwayland-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
%{?with_tests:BuildRequires:	kf5-sonnet-devel >= %{kf_ver}}
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick-controls2 >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	kf5-dirs
Requires:	kf5-kactivities >= %{kf_ver}
Requires:	kf5-karchive >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kconfigwidgets >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kdbusaddons >= %{kf_ver}
Requires:	kf5-kdeclarative >= %{kf_ver}
Requires:	kf5-kdoctools >= %{kf_ver}
Requires:	kf5-kglobalaccel >= %{kf_ver}
Requires:	kf5-kguiaddons >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kiconthemes >= %{kf_ver}
Requires:	kf5-kio >= %{kf_ver}
Requires:	kf5-kirigami2 >= %{kf_ver}
Requires:	kf5-knotifications >= %{kf_ver}
Requires:	kf5-kpackage >= %{kf_ver}
Requires:	kf5-kservice >= %{kf_ver}
Requires:	kf5-kwayland >= %{kf_ver}
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
# >= to allow also kf6-libplasma-data
Requires:	kf5-plasma-desktoptheme-breeze >= %{version}-%{release}
Suggests:	kf5-plasma-desktoptheme-air = %{version}-%{release}
# >= to allow also kp6-oxygen
Suggests:	kf5-plasma-desktoptheme-oxygen >= %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Plasma framework provides the foundations that can be used to
build a primary user interface, from graphical to logical components.

The Plasma framework provides the following:
- A C++ library: libplasma
- Script engines
- QML components

%description -l pl.UTF-8
Szkielet Plasma dostarcza podstawowe konstrukcje, których można użyć
do zbudowania głównego interfejsu użytkownika, od komponentów
graficznych po logiczne.

Szkielet Plasma zawiera:
- bibliotekę C++ libplasma
- silniki skryptowe
- komponenty QML

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Gui-devel >= %{qt_ver}
Requires:	Qt5Qml-devel >= %{qt_ver}
Requires:	Qt5Quick-devel >= %{qt_ver}
Requires:	kf5-extra-cmake-modules >= %{kf_ver}
Requires:	kf5-kconfig-devel >= %{kf_ver}
Requires:	kf5-kcoreaddons-devel >= %{kf_ver}
Requires:	kf5-kpackage-devel >= %{kf_ver}
Requires:	kf5-kservice-devel >= %{kf_ver}
Requires:	kf5-kwindowsystem-devel >= %{kf_ver}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%package -n kf5-plasma-desktoptheme-air
Summary:	Air desktop theme for Plasma
Summary(pl.UTF-8):	Motyw pulpitu Air dla Plasmy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n kf5-plasma-desktoptheme-air
Air desktop theme for Plasma.

%description -n kf5-plasma-desktoptheme-air -l pl.UTF-8
Motyw pulpitu Air dla Plasmy.

%package -n kf5-plasma-desktoptheme-breeze
Summary:	Breeze desktop themes for Plasma
Summary(pl.UTF-8):	Motywy pulpitu Breeze dla Plasmy
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Conflicts:	kp6-libplasma-data

%description -n kf5-plasma-desktoptheme-breeze
Breeze (default, dark and light) desktop themes for Plasma.

%description -n kf5-plasma-desktoptheme-breeze -l pl.UTF-8
Motywy pulpitu Breeze dla Plasmy (domyślny, ciemny i jasny).

%package -n kf5-plasma-desktoptheme-oxygen
Summary:	Oxygen desktop theme for Plasma
Summary(pl.UTF-8):	Motyw pulpitu Oxygen dla Plasmy
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Conflicts:	kp6-oxygen

%description -n kf5-plasma-desktoptheme-oxygen
Oxygen desktop theme for Plasma.

%description -n kf5-plasma-desktoptheme-oxygen -l pl.UTF-8
Motyw pulpitu Oxygen dla Plasmy.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -d $RPM_BUILD_ROOT%{_libdir}/qt5/plugins/plasma/applets

%find_lang libplasma5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libplasma5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/plasmapkg2
%attr(755,root,root) %{_libdir}/libKF5Plasma.so.*.*
%ghost %{_libdir}/libKF5Plasma.so.5
%attr(755,root,root) %{_libdir}/libKF5PlasmaQuick.so.*.*
%ghost %{_libdir}/libKF5PlasmaQuick.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kirigami/KirigamiPlasmaStyle.so
%dir %{_libdir}/qt5/plugins/kpackage/packagestructure
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_applet.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_containmentactions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_dataengine.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_generic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_theme.so
%dir %{_libdir}/qt5/plugins/plasma
%dir %{_libdir}/qt5/plugins/plasma/applets
%dir %{_libdir}/qt5/plugins/plasma/scriptengines
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/scriptengines/plasma_appletscript_declarative.so
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Plasma
%dir %{_libdir}/qt5/qml/QtQuick/Controls.2/Plasma
%{_libdir}/qt5/qml/QtQuick/Controls.2/Plasma/*.qml
%{_libdir}/qt5/qml/QtQuick/Controls.2/Plasma/README.md
%{_libdir}/qt5/qml/QtQuick/Controls.2/Plasma/mobiletextselection
%{_libdir}/qt5/qml/QtQuick/Controls.2/Plasma/private
%{_libdir}/qt5/qml/QtQuick/Controls.2/Plasma/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kirigami.2/styles/Plasma
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/Plasma/*.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma
%{_libdir}/qt5/qml/org/kde/plasma/accessdenied
%dir %{_libdir}/qt5/qml/org/kde/plasma/calendar
%{_libdir}/qt5/qml/org/kde/plasma/calendar/*.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/calendar/libcalendarplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/calendar/plugins.qmltypes
%{_libdir}/qt5/qml/org/kde/plasma/calendar/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/components
%{_libdir}/qt5/qml/org/kde/plasma/components/*.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/*.js
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/components/libplasmacomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/components/plugins.qmltypes
%{_libdir}/qt5/qml/org/kde/plasma/components/private
%{_libdir}/qt5/qml/org/kde/plasma/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/components.3
%{_libdir}/qt5/qml/org/kde/plasma/components.3/*.qml
%{_libdir}/qt5/qml/org/kde/plasma/components.3/README.md
%{_libdir}/qt5/qml/org/kde/plasma/components.3/mobiletextselection
%{_libdir}/qt5/qml/org/kde/plasma/components.3/private
%{_libdir}/qt5/qml/org/kde/plasma/components.3/qmldir
%dir  %{_libdir}/qt5/qml/org/kde/plasma/core
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/core/libcorebindingsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/core/plugins.qmltypes
%{_libdir}/qt5/qml/org/kde/plasma/core/private
%{_libdir}/qt5/qml/org/kde/plasma/core/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/extras
%{_libdir}/qt5/qml/org/kde/plasma/extras/*.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/extras/plugins.qmltypes
%{_libdir}/qt5/qml/org/kde/plasma/extras/private
%{_libdir}/qt5/qml/org/kde/plasma/extras/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/platformcomponents
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/libplatformcomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/plugins.qmltypes
%{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/qmldir
%{_datadir}/kservicetypes5/plasma-applet.desktop
%{_datadir}/kservicetypes5/plasma-containment.desktop
%{_datadir}/kservicetypes5/plasma-containmentactions.desktop
%{_datadir}/kservicetypes5/plasma-dataengine.desktop
%{_datadir}/kservicetypes5/plasma-generic.desktop
%{_datadir}/kservicetypes5/plasma-lookandfeel.desktop
%{_datadir}/kservicetypes5/plasma-packagestructure.desktop
%{_datadir}/kservicetypes5/plasma-scriptengine.desktop
%{_datadir}/kservicetypes5/plasma-service.desktop
%{_datadir}/kservicetypes5/plasma-shell.desktop
%{_datadir}/kservicetypes5/plasma-wallpaper.desktop
%dir %{_datadir}/plasma/services
%{_datadir}/plasma/services/dataengineservice.operations
%{_datadir}/plasma/services/plasmoidservice.operations
%{_datadir}/plasma/services/storage.operations
%{_datadir}/qlogging-categories5/plasma-framework.categories
%{_datadir}/qlogging-categories5/plasma-framework.renamecategories
%{_mandir}/man1/plasmapkg2.1*
%lang(ca) %{_mandir}/ca/man1/plasmapkg2.1*
%lang(ca) %{_mandir}/ca@valencia/man1/plasmapkg2.1*
%lang(de) %{_mandir}/de/man1/plasmapkg2.1*
%lang(es) %{_mandir}/es/man1/plasmapkg2.1*
%lang(fr) %{_mandir}/fr/man1/plasmapkg2.1*
%lang(it) %{_mandir}/it/man1/plasmapkg2.1*
%lang(nl) %{_mandir}/nl/man1/plasmapkg2.1*
%lang(pt) %{_mandir}/pt/man1/plasmapkg2.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/plasmapkg2.1*
%lang(sv) %{_mandir}/sv/man1/plasmapkg2.1*
%lang(uk) %{_mandir}/uk/man1/plasmapkg2.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKF5Plasma.so
%{_libdir}/libKF5PlasmaQuick.so
%{_includedir}/KF5/Plasma
%{_includedir}/KF5/plasma
%{_includedir}/KF5/PlasmaQuick
%{_includedir}/KF5/plasmaquick
%{_libdir}/cmake/KF5Plasma
%{_libdir}/cmake/KF5PlasmaQuick
%{_datadir}/kdevappwizard/templates/cpp-plasmoid.tar.bz2
%{_datadir}/kdevappwizard/templates/plasma-wallpaper.tar.bz2
%{_datadir}/kdevappwizard/templates/plasma-wallpaper-with-qml-extension.tar.bz2
%{_datadir}/kdevappwizard/templates/qml-plasmoid-with-qml-extension.tar.bz2
%{_datadir}/kdevappwizard/templates/qml-plasmoid.tar.bz2

%files -n kf5-plasma-desktoptheme-air
%defattr(644,root,root,755)
%{_datadir}/plasma/desktoptheme/air

%files -n kf5-plasma-desktoptheme-breeze
%defattr(644,root,root,755)
%dir %{_datadir}/plasma/desktoptheme
%{_datadir}/plasma/desktoptheme/breeze-dark
%{_datadir}/plasma/desktoptheme/breeze-light
%{_datadir}/plasma/desktoptheme/default

%files -n kf5-plasma-desktoptheme-oxygen
%defattr(644,root,root,755)
%{_datadir}/plasma/desktoptheme/oxygen
