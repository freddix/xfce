Summary:	XFCE desktop
Name:		xfce
Version:	4.10.0
Release:	5
License:	GPL v2
Group:		X11/Applications
Source0:	xfce4.target
Source1:	xfce4-session.service
Source2:	xfwm4.service
# core
Requires:	Thunar >= 1.4.0
Requires:	exo >= 0.8.0
Requires:	garcon >= 0.2.0
Requires:	thunar-plugin-volman >= 0.8.0
Requires:	tumbler
Requires:	xfce4-appfinder >= 4.10.0
Requires:	xfce4-panel >= 4.10.0
Requires:	xfce4-power-manager >= 1.2.0
Requires:	xfce4-preferred-applications
Requires:	xfce4-session >= 4.10.0
Requires:	xfce4-settings >= 4.10.0
Requires:	xfconf >= 4.10.0
Requires:	xfdesktop >= 4.10.0
Requires:	xfwm4 >= 4.10.0
# additional components
Requires:	parole
Requires:	xfce4-screenshooter
Requires:	xfce4-taskmanager
# xdg-notification-daemon
Suggests:	xfce4-notifyd
# some nice panel plugins
Requires:	xfce4-plugin-cpugraph
Requires:	xfce4-plugin-notes
Requires:	xfce4-plugin-screenshooter
Requires:	xfce4-plugin-weather
Requires:	xfce4-plugin-xkb
# systemd user session
Suggests:	xorg-launch-helper
# desktop environment
Requires:	desktop-file-utils
Requires:	xdg-icon-theme
Requires:	xdg-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip			1
%define		no_install_post_chrpath			1
%define		no_install_post_compress_modules	1

%define		_enable_debug_packages	0

%description
XFCE %{version} desktop.

%prep
%build
%install
install -d $RPM_BUILD_ROOT%{_prefix}/lib/systemd/user/xfce4.target.wants

install %{SOURCE0} %{SOURCE1} %{SOURCE2} \
	$RPM_BUILD_ROOT%{_prefix}/lib/systemd/user

ln -s %{_prefix}/lib/systemd/user/xfce4-session.service \
	$RPM_BUILD_ROOT%{_prefix}/lib/systemd/user/xfce4.target.wants/xfce4-session.service

ln -s %{_prefix}/lib/systemd/user/xfwm4.service \
	$RPM_BUILD_ROOT%{_prefix}/lib/systemd/user/xfce4.target.wants/xfwm4.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/lib/systemd/user/xfce4.target
%{_prefix}/lib/systemd/user/xfce4-session.service
%{_prefix}/lib/systemd/user/xfwm4.service
%dir %{_prefix}/lib/systemd/user/xfce4.target.wants
%{_prefix}/lib/systemd/user/xfce4.target.wants/xfce4-session.service
%{_prefix}/lib/systemd/user/xfce4.target.wants/xfwm4.service

