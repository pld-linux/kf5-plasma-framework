#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeframever	5.116
%define		qtver		5.15.2
%define		kfname		plasma-framework

Summary:	The foundations that can be used to build a primary user interface
Summary(pl.UTF-8):	Podstawowe konstrukcje do zbudowania głównego interfejsu użytkownika
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	425fd39b0b689e60690feb514739d605
URL:		https://kde.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kactivities-devel >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdeclarative-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kirigami2-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kpackage-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwayland-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

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
Requires:	kf5-kpackage-devel >= %{version}
Requires:	kf5-kservice-devel >= %{version}
Requires:	kf5-kwindowsystem-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

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
%{_mandir}/ca/man1/plasmapkg2.1*
%{_mandir}/de/man1/plasmapkg2.1*
%{_mandir}/es/man1/plasmapkg2.1*
%{_mandir}/fr/man1/plasmapkg2.1*
%{_mandir}/it/man1/plasmapkg2.1*
%{_mandir}/nl/man1/plasmapkg2.1*
%{_mandir}/pt/man1/plasmapkg2.1*
%{_mandir}/pt_BR/man1/plasmapkg2.1*
%{_mandir}/sv/man1/plasmapkg2.1*
%{_mandir}/uk/man1/plasmapkg2.1*

# themes
%dir %{_datadir}/plasma/desktoptheme
%{_datadir}/plasma/desktoptheme/air
%{_datadir}/plasma/desktoptheme/breeze-dark
%{_datadir}/plasma/desktoptheme/breeze-light
%{_datadir}/plasma/desktoptheme/default
%{_datadir}/plasma/desktoptheme/oxygen

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
