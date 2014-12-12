%define         kdeframever     5.4
%define         qtver           5.3.2
%define         kfname          plasma-framework

Summary:	The foundations that can be used to build a primary user interface
Name:		kf5-%{kfname}
Version:	5.4.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	f55da2ff4612bbe6c920aef0ec31d29d
URL:		http://www.kde.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
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
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
The plasma framework provides the foundations that can be used to
build a primary user interface, from graphical to logical components.

The plasma framework provides the following:
- A C++ library: libplasma
- Script engines
- QML components


%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/dpitest
%attr(755,root,root) %{_bindir}/plasmapkg2
%attr(755,root,root) %ghost %{_libdir}/libKF5Plasma.so.5
%attr(755,root,root) %{_libdir}/libKF5Plasma.so.5.4.0
%attr(755,root,root) %ghost %{_libdir}/libKF5PlasmaQuick.so.5
%attr(755,root,root) %{_libdir}/libKF5PlasmaQuick.so.5.4.0
%dir %{_libdir}/qt5/platformqml/touch/org/kde/plasma/components
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/BusyIndicator.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Button.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ButtonColumn.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ButtonGroup.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ButtonRow.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/CheckBox.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/CommonDialog.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Dialog.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/EditBubble.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/EditBubble.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Highlight.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Label.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ListItem.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Menu.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/MenuItem.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Page.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/PageStack.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ProgressBar.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/QueryDialog.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/RadioButton.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ScrollBar.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ScrollDecorator.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/SectionScroller.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/SelectionDialog.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Sheet.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Slider.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Switch.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/TabBar.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/TabButton.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/TabGroup.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/TextArea.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/TextField.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/TextFieldFocus.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ToolBar.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ToolBarLayout.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/ToolButton.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/Window.qml
%attr(755,root,root) %{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/libplasmacomponentsplugin.so
%dir %{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/AppManager.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/ButtonShadow.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/Config.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/DualStateButton.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/InlineDialog.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/PageStack.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/RoundShadow.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/ScrollBarDelegate.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/ScrollDecoratorDelegate.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/SectionScroller.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/TabBarLayout.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/TabGroup.js
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/private/TextFieldFocus.qml
%{_libdir}/qt5/platformqml/touch/org/kde/plasma/components/qmldir
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/platformstatus.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_appletscript_declarative.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_engine_testengine.so
%dir %{_libdir}/qt5/qml/org/kde/plasma
%{_libdir}/qt5/qml/org/kde/plasma/accessdenied
%dir %{_libdir}/qt5/qml/org/kde/plasma/calendar
%{_libdir}/qt5/qml/org/kde/plasma/calendar/CalendarToolbar.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/DayDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/DaysCalendar.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/MonthMenu.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/MonthView.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/calendar/libcalendarplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/calendar/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/components
%{_libdir}/qt5/qml/org/kde/plasma/components/BusyIndicator.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Button.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ButtonColumn.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ButtonGroup.js
%{_libdir}/qt5/qml/org/kde/plasma/components/ButtonRow.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/CheckBox.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ComboBox.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/CommonDialog.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ContextMenu.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Dialog.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Highlight.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Label.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ListItem.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ModelContextMenu.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Page.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/PageStack.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ProgressBar.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/QueryDialog.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/RadioButton.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ScrollBar.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/SectionScroller.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/SelectionDialog.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Sheet.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Slider.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/Switch.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/TabBar.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/TabButton.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/TabGroup.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/TextArea.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/TextField.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ToolBar.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ToolBarLayout.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/ToolButton.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/components/libplasmacomponentsplugin.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/components/private
%{_libdir}/qt5/qml/org/kde/plasma/components/private/AppManager.js
%{_libdir}/qt5/qml/org/kde/plasma/components/private/ButtonShadow.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/Config.js
%{_libdir}/qt5/qml/org/kde/plasma/components/private/DualStateButton.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/InlineDialog.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/PageStack.js
%{_libdir}/qt5/qml/org/kde/plasma/components/private/RoundShadow.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/ScrollBarDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/ScrollDecoratorDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/SectionScroller.js
%{_libdir}/qt5/qml/org/kde/plasma/components/private/TabBarLayout.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/private/TabGroup.js
%{_libdir}/qt5/qml/org/kde/plasma/components/private/TextFieldFocus.qml
%{_libdir}/qt5/qml/org/kde/plasma/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/components/styles
%{_libdir}/qt5/qml/org/kde/plasma/components/styles/*.qml
%dir  %{_libdir}/qt5/qml/org/kde/plasma/core
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/core/libcorebindingsplugin.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/core/private
%{_libdir}/qt5/qml/org/kde/plasma/core/private/DefaultToolTip.qml
%{_libdir}/qt5/qml/org/kde/plasma/core/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/extras
%{_libdir}/qt5/qml/org/kde/plasma/extras/App.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/ConditionalLoader.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/Heading.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/PageRow.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/Paragraph.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/ScrollArea.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/Title.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma/extras/animations
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/ActivateAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/AppearAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/DisappearAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/PressedAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/ReleasedAnimation.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/extras/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/platformcomponents
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/libplatformcomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/qmldir
%{_datadir}/dbus-1/interfaces/org.kde.platformstatus.xml
%{_datadir}/kservices5/kded/kded_platformstatus.desktop
%{_datadir}/kservices5/plasma-dataengine-testengine.desktop
%{_datadir}/kservices5/plasma-scriptengine-applet-declarative.desktop
%{_datadir}/kservices5/plasma-scriptengine-ruby-dataengine.desktop
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
%{_mandir}/man1/plasmapkg2.1*
%dir %{_datadir}/plasma
%dir %{_datadir}/plasma/desktoptheme
%{_datadir}/plasma/desktoptheme/air
%{_datadir}/plasma/desktoptheme/breeze-dark
%{_datadir}/plasma/desktoptheme/default
%{_datadir}/plasma/desktoptheme/oxygen
%{_datadir}/plasma/plasma_scriptengine_ruby
%dir %{_datadir}/plasma/services
%{_datadir}/plasma/services/dataengineservice.operations
%{_datadir}/plasma/services/plasmoidservice.operations
%{_datadir}/plasma/services/storage.operations

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Plasma
%{_includedir}/KF5/plasma
%{_includedir}/KF5/plasma_version.h
%{_libdir}/cmake/KF5Plasma
%{_libdir}/cmake/KF5PlasmaQuick
%attr(755,root,root) %{_libdir}/libKF5Plasma.so
%attr(755,root,root) %{_libdir}/libKF5PlasmaQuick.so
