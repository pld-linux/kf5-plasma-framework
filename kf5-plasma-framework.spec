# TODO: split

%define         _state          stable
%define		orgname		plasma-framework

Summary:	The foundations that can be used to build a primary user interface
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	088643662f7e60b5cafe2f26182882eb
URL:		http://www.kde.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.3.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel >= 5.2.0
BuildRequires:	Qt5Widgets-devel >= 5.3.1
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel >= 5.2.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 0.0.9
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
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	-D_IMPORT_PREFIX=%{_prefix} \
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
%attr(755,root,root) %{_libdir}/libKF5Plasma.so.5.0.0
%attr(755,root,root) %ghost %{_libdir}/libKF5PlasmaQuick.so.5
%attr(755,root,root) %{_libdir}/libKF5PlasmaQuick.so.5.0.0
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
%{_libdir}/qt5/qml/org/kde/plasma/accessdenied/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/calendar/CalendarToolbar.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/DayDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/DaysCalendar.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/MonthMenu.qml
%{_libdir}/qt5/qml/org/kde/plasma/calendar/MonthView.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/calendar/libcalendarplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/calendar/qmldir
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
%{_libdir}/qt5/qml/org/kde/plasma/components/styles/ComboBoxStyle.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/core/libcorebindingsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/core/private/DefaultToolTip.qml
%{_libdir}/qt5/qml/org/kde/plasma/core/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/extras/App.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/ConditionalLoader.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/Heading.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/PageRow.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/Paragraph.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/ScrollArea.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/Title.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/ActivateAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/AppearAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/DisappearAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/PressedAnimation.qml
%{_libdir}/qt5/qml/org/kde/plasma/extras/animations/ReleasedAnimation.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/extras/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/extras/styles/ScrollViewStyle.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/libplatformcomponentsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/platformcomponents/qmldir
%{_datadir}/dbus-1/interfaces/org.kde.platformstatus.xml
%{_datadir}/kservices5/kded/kded_platformstatus.desktop
%{_datadir}/kservices5/plasma-dataengine-testengine.desktop
%{_datadir}/kservices5/plasma-scriptengine-applet-declarative.desktop
%{_datadir}/kservices5/plasma-scriptengine-ruby-dataengine.desktop
%{_datadir}/kservices5/plasma-wallpaper.desktop
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
%{_mandir}/man1/plasmapkg2.1*
%{_datadir}/plasma/desktoptheme/air/colors
%{_datadir}/plasma/desktoptheme/air/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/air/dialogs/kickoff.svgz
%{_datadir}/plasma/desktoptheme/air/dialogs/krunner.svgz
%{_datadir}/plasma/desktoptheme/air/icons/amarok.svgz
%{_datadir}/plasma/desktoptheme/air/icons/audio.svgz
%{_datadir}/plasma/desktoptheme/air/icons/battery.svgz
%{_datadir}/plasma/desktoptheme/air/icons/configure.svgz
%{_datadir}/plasma/desktoptheme/air/icons/device.svgz
%{_datadir}/plasma/desktoptheme/air/icons/document.svgz
%{_datadir}/plasma/desktoptheme/air/icons/edit.svgz
%{_datadir}/plasma/desktoptheme/air/icons/go.svgz
%{_datadir}/plasma/desktoptheme/air/icons/kget.svgz
%{_datadir}/plasma/desktoptheme/air/icons/klipper.svgz
%{_datadir}/plasma/desktoptheme/air/icons/konv_message.svgz
%{_datadir}/plasma/desktoptheme/air/icons/konversation.svgz
%{_datadir}/plasma/desktoptheme/air/icons/kopete.svgz
%{_datadir}/plasma/desktoptheme/air/icons/korgac.svgz
%{_datadir}/plasma/desktoptheme/air/icons/kpackagekit.svgz
%{_datadir}/plasma/desktoptheme/air/icons/ktorrent.svgz
%{_datadir}/plasma/desktoptheme/air/icons/list.svgz
%{_datadir}/plasma/desktoptheme/air/icons/media.svgz
%{_datadir}/plasma/desktoptheme/air/icons/nepomuk.svgz
%{_datadir}/plasma/desktoptheme/air/icons/network.svgz
%{_datadir}/plasma/desktoptheme/air/icons/notification.svgz
%{_datadir}/plasma/desktoptheme/air/icons/preferences.svgz
%{_datadir}/plasma/desktoptheme/air/icons/printer.svgz
%{_datadir}/plasma/desktoptheme/air/icons/quassel.svgz
%{_datadir}/plasma/desktoptheme/air/icons/slc.svgz
%{_datadir}/plasma/desktoptheme/air/icons/wallet.svgz
%{_datadir}/plasma/desktoptheme/air/icons/window.svgz
%{_datadir}/plasma/desktoptheme/air/icons/zoom.svgz
%{_datadir}/plasma/desktoptheme/air/metadata.desktop
%{_datadir}/plasma/desktoptheme/air/opaque/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/air/opaque/dialogs/krunner.svgz
%{_datadir}/plasma/desktoptheme/air/opaque/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/air/opaque/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/air/opaque/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/air/translucent/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/air/translucent/dialogs/krunner.svgz
%{_datadir}/plasma/desktoptheme/air/translucent/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/air/translucent/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/air/translucent/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/action-overlays.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/actionbutton.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/analog_meter.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/arrows.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/bar_meter_horizontal.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/bar_meter_vertical.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/branding.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/busywidget.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/button.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/calendar.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/checkmarks.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/clock.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/configuration-icons.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/containment-controls.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/dragger.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/extender-dragger.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/frame.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/glowbar.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/identiconshapes.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/identicontheme.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/labeltexture.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/line.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/lineedit.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/listitem.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/media-delegate.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/monitor.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/pager.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/picker.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/plot-background.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/scrollbar.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/scrollwidget.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/slider.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/systemtray.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/tabbar.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/tasks.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/toolbar.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/toolbox.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/translucentbackground.svgz
%{_datadir}/plasma/desktoptheme/air/widgets/viewitem.svgz
%{_datadir}/plasma/desktoptheme/breeze-dark/colors
%{_datadir}/plasma/desktoptheme/breeze-dark/metadata.desktop
%{_datadir}/plasma/desktoptheme/default/colors
%{_datadir}/plasma/desktoptheme/default/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/default/icons/akonadi.svgz
%{_datadir}/plasma/desktoptheme/default/icons/akregator.svgz
%{_datadir}/plasma/desktoptheme/default/icons/amarok.svgz
%{_datadir}/plasma/desktoptheme/default/icons/applications.svgz
%{_datadir}/plasma/desktoptheme/default/icons/apport.svgz
%{_datadir}/plasma/desktoptheme/default/icons/audio.svgz
%{_datadir}/plasma/desktoptheme/default/icons/battery.svgz
%{_datadir}/plasma/desktoptheme/default/icons/bookmarks.svgz
%{_datadir}/plasma/desktoptheme/default/icons/computer.svgz
%{_datadir}/plasma/desktoptheme/default/icons/configure.svgz
%{_datadir}/plasma/desktoptheme/default/icons/device.svgz
%{_datadir}/plasma/desktoptheme/default/icons/document.svgz
%{_datadir}/plasma/desktoptheme/default/icons/drive.svgz
%{_datadir}/plasma/desktoptheme/default/icons/edit.svgz
%{_datadir}/plasma/desktoptheme/default/icons/go.svgz
%{_datadir}/plasma/desktoptheme/default/icons/input.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kdeconnect.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kget.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kgpg.svgz
%{_datadir}/plasma/desktoptheme/default/icons/klipper.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kmail.svgz
%{_datadir}/plasma/desktoptheme/default/icons/konv_message.svgz
%{_datadir}/plasma/desktoptheme/default/icons/konversation.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kopete.svgz
%{_datadir}/plasma/desktoptheme/default/icons/korgac.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kpackagekit.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kteatime.svgz
%{_datadir}/plasma/desktoptheme/default/icons/ktorrent.svgz
%{_datadir}/plasma/desktoptheme/default/icons/list.svgz
%{_datadir}/plasma/desktoptheme/default/icons/mail.svgz
%{_datadir}/plasma/desktoptheme/default/icons/media.svgz
%{_datadir}/plasma/desktoptheme/default/icons/nepomuk.svgz
%{_datadir}/plasma/desktoptheme/default/icons/network.svgz
%{_datadir}/plasma/desktoptheme/default/icons/notification.svgz
%{_datadir}/plasma/desktoptheme/default/icons/phone.svgz
%{_datadir}/plasma/desktoptheme/default/icons/preferences.svgz
%{_datadir}/plasma/desktoptheme/default/icons/printer.svgz
%{_datadir}/plasma/desktoptheme/default/icons/quassel.svgz
%{_datadir}/plasma/desktoptheme/default/icons/slc.svgz
%{_datadir}/plasma/desktoptheme/default/icons/software-updates.svgz
%{_datadir}/plasma/desktoptheme/default/icons/start.svgz
%{_datadir}/plasma/desktoptheme/default/icons/system.svgz
%{_datadir}/plasma/desktoptheme/default/icons/touchpad.svgz
%{_datadir}/plasma/desktoptheme/default/icons/user.svgz
%{_datadir}/plasma/desktoptheme/default/icons/video.svgz
%{_datadir}/plasma/desktoptheme/default/icons/view.svgz
%{_datadir}/plasma/desktoptheme/default/icons/wallet.svgz
%{_datadir}/plasma/desktoptheme/default/icons/window.svgz
%{_datadir}/plasma/desktoptheme/default/icons/zoom.svgz
%{_datadir}/plasma/desktoptheme/default/metadata.desktop
%{_datadir}/plasma/desktoptheme/default/opaque/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/default/opaque/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/opaque/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/default/translucent/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/default/translucent/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/translucent/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/action-overlays.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/actionbutton.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/analog_meter.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/arrows.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/bar_meter_horizontal.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/bar_meter_vertical.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/branding.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/busywidget.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/button.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/calendar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/checkmarks.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/clock.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/configuration-icons.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/containment-controls.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/dragger.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/frame.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/glowbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/line.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/lineedit.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/listitem.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/media-delegate.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/monitor.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/pager.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/picker.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/plot-background.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/scrollbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/scrollwidget.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/slider.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/tabbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/tasks.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/toolbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/translucentbackground.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/viewitem.svgz
%{_datadir}/plasma/desktoptheme/oxygen/colors
%{_datadir}/plasma/desktoptheme/oxygen/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/dialogs/kickoff.svgz
%{_datadir}/plasma/desktoptheme/oxygen/dialogs/krunner.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/amarok.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/audio.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/battery.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/configure.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/device.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/document.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/edit.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/go.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/kget.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/klipper.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/konv_message.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/konversation.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/kopete.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/korgac.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/kpackagekit.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/ktorrent.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/list.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/media.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/nepomuk.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/network.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/notification.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/preferences.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/printer.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/quassel.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/slc.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/wallet.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/window.svgz
%{_datadir}/plasma/desktoptheme/oxygen/icons/zoom.svgz
%{_datadir}/plasma/desktoptheme/oxygen/metadata.desktop
%{_datadir}/plasma/desktoptheme/oxygen/opaque/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/dialogs/krunner.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/action-overlays.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/actionbutton.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/analog_meter.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/arrows.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/bar_meter_horizontal.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/bar_meter_vertical.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/branding.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/busywidget.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/button.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/calendar.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/clock.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/configuration-icons.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/containment-controls.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/dragger.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/extender-dragger.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/frame.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/glowbar.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/line.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/lineedit.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/media-delegate.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/monitor.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/pager.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/plot-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/scrollbar.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/scrollwidget.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/slider.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/systemtray.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/tasks.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/timer.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/toolbox.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/translucentbackground.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/viewitem.svgz
%{_datadir}/plasma/plasma_scriptengine_ruby/data_engine.rb
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
