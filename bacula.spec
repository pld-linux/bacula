#
# TODO:
#	- update desktop files, think about su-wrappers for console
Summary:	Bacula - The Network Backup Solution
Summary(pl):	Bacula - rozwi±zanie do wykonywania kopii zapasowych po sieci
Name:		bacula
Version:	1.36.2
Release:	1
Epoch:		0
Group:		Networking/Utilities
License:	extended GPL v2
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	55a9ab6d211913fa8c73e3d07eabc189
Source1:	%{name}-manpages.tar.bz2
# Source1-md5:	e4dae86d6574b360e831efd3913e7f4c
Source10:	%{name}-dir.init
Source11:	%{name}-fd.init
Source12:	%{name}-sd.init
Source13:	%{name}.logrotate
Source14:	%{name}-dir.sysconfig
Source15:	%{name}-fd.sysconfig
Source16:	%{name}-sd.sysconfig
URL:		http://www.bacula.org/
BuildRequires:	acl-static
BuildRequires:	automake
BuildRequires:	glibc-static
BuildRequires:	libgnome-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libstdc++-static
BuildRequires:	libwrap-static
BuildRequires:	mtx
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite-devel
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRequires:	wxGTK2-devel < 2.5.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_localstatedir	/var/lib/%{name}

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

%description -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula to zbiór programów umo¿liwiaj±cych administratorowi na
zarz±dzanie kopiami zapasowymi, odzyskiwaniem i weryfikacj± danych
w sieci komputerów ró¿nego rodzaju. W terminologii technicznej jest to
program do kopii zapasowych pracuj±cy w architekturze klient-serwer.
Bacula jest stosunkowo ³atwa w u¿yciu i wydajna, oferuj±c przy tym
wiele zaawansowanych mo¿liwo¶ci przy zarz±dzaniu no¶nikami,
u³atwiaj±cych znalezienie i odzyskanie utraconych lub uszkodzonych
plików.

%package common
Summary:	Common files for bacula package
Summary(pl):	Pliki wspólne dla pakietu bacula
Group:		Networking/Utilities
Conflicts:	bacula-dir < 0:1.34.6
Conflicts:	bacula-fd < 0:1.34.6
Conflicts:	bacula-sd < 0:1.34.6
Conflicts:	bacula-console < 0:1.34.6
Requires(post):	openssl-tools
Requires(post):	sed >= 4.0

%description common
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

%description common -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula to zbiór programów umo¿liwiaj±cych administratorowi na
zarz±dzanie kopiami zapasowymi, odzyskiwaniem i weryfikacj± danych
w sieci komputerów ró¿nego rodzaju. W terminologii technicznej jest to
program do kopii zapasowych pracuj±cy w architekturze klient-serwer.
Bacula jest stosunkowo ³atwa w u¿yciu i wydajna, oferuj±c przy tym
wiele zaawansowanych mo¿liwo¶ci przy zarz±dzaniu no¶nikami,
u³atwiaj±cych znalezienie i odzyskanie utraconych lub uszkodzonych
plików.

%package dir
Summary:	Bacula Director and Catalog services
Summary(pl):	Us³ugi Bacula Director i Catalog
Group:		Networking/Utilities
Obsoletes:	%{name}-updatedb
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description dir
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Director is the program that supervises all the backup,
restore, verify and archive operations. The system administrator uses
the Bacula Director to schedule backups and to recover files. Catalog
services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed
up. The Catalog services permit the System Administrator or user to
quickly locate and restore any desired file, since it maintains a
record of all Volumes used, all Jobs run, and all Files saved. This
build requires sqlite to be installed separately as the catalog
database.

%description dir -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula Director to program nadzoruj±cy wszystkie operacje wykonywania
kopii zapasowych, odzyskiwania, weryfikacji i archiwizowania.
Administrator u¿ywa Bacula Directora do szeregowania kopii zapasowych
oraz odzyskiwania plików. Us³ugi katalogowe (Catalog services) s±
u¿ywane przez programy odpowiedzialne za zarz±dzanie indeksami plików
i baz± danych wolumenów dla wszystkich kopiowanych plików. Us³ugi
katalogowe umo¿liwiaj± administratorowi lub u¿ytkownikowi szybko
zlokalizowaæ i odtworzyæ dowolny plik, poniewa¿ utrzymuj± rekord ze
wszystkimi u¿ywanymi wolumenami, uruchomionymi zadaniami i zapisanymi
plikami. Pakiet wymaga sqlite zainstalowanego oddzielnie jako bazy
danych dla katalogu.

%package console
Summary:	Bacula Console
Summary(pl):	Konsola Baculi
Group:		Networking/Utilities
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description console
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the text only console
interface.

%description console -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula Console to program umo¿liwiaj±cy administratorowi lub
u¿ytkownikowi komunikowanie siê z programem Bacula Director. To jest
interfejs czysto tekstowy.

%package console-wx
Summary:	Bacula wxWidgets Console
Summary(pl):	Konsola Baculi oparta na wxWidgets
Group:		Networking/Utilities
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description console-wx
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the wxWidgets GUI
interface.

%description console-wx -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula Console to program umo¿liwiaj±cy administratorowi lub
u¿ytkownikowi komunikowanie siê z programem Bacula Director. To jest
interfejs graficzny oparty na wxWidgets.

%package console-gnome
Summary:	Bacula GNOME Console
Summary(pl):	Konsola Baculi oparta dla GNOME
Group:		Networking/Utilities
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description console-gnome
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the GNOME GUI
interface.

%description console-gnome -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula Console to program umo¿liwiaj±cy administratorowi lub
u¿ytkownikowi komunikowanie siê z programem Bacula Director. To jest
interfejs graficzny oparty na GNOME.

%package tray-monitor
Summary:	Bacula Tray Monitor
Group:		Networking/Utilities
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description tray-monitor
Bacula - It comes by night and sucks the vital essence from your
computers.

The Monitor program is typically an icon in the system tray. However, once the
icon is expanded into a full window, the administrator or user can obtain
status information about the Director or the backup status on the local
workstation or any other Bacula daemon that is configured.

%package fd
Summary:	Bacula File services (Client)
Summary(pl):	Us³ugi Bacula File (klient)
Group:		Networking/Utilities
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description fd
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula File services (or Client program) is the software program that
is installed on the machine to be backed up. It is specific to the
operating system on which it runs and is responsible for providing the
file attributes and data when requested by the Director. The File
services are also responsible for the file system dependent part of
restoring the file attributes and data during a recovery operation.
This program runs as a daemon on the machine to be backed up, and in
some of the documentation, the File daemon is referred to as the
Client (for example in Bacula configuration file).

%description fd -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Us³ugi Bacula File (inaczej program kliencki) to oprogramowanie, które
instaluje siê na maszynach, z których maj± byæ wykonywane kopie
zapasowe. S± one specyficzne dla systemu operacyjnego, pod którym
dzia³a dana maszyna i odpowiadaj± za dostarczanie atrybutów i danych
plików na ¿±danie Directora. Us³ugi plikowe s± tak¿e odpowiedzialne za
zale¿n± od systemu plików czê¶æ odzyskiwania atrybutów i danych plików
podczas operacji odzyskiwania danych. Program dzia³a jako demon na
maszynie, która ma byæ backupowana i w czê¶ci dokumentacji demon ten
(File) jest nazywany klientem (na przyk³ad w pliku konfiguracyjnym
Baculi).

%package sd
Summary:	Bacula Storage services
Summary(pl):	Us³ugi Bacula Storage
Group:		Networking/Utilities
PreReq:		bacula-common = %{epoch}:%{version}-%{release}
Requires(post):	sed >= 4.0

%description sd
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Storage services consist of the software programs that perform
the storage and recovery of the file attributes and data to the
physical backup media or volumes. In other words, the Storage daemon
is responsible for reading and writing your tapes (or other storage
media, e.g. files). The Storage services runs as a daemon on the
machine that has the backup device (usually a tape drive).

%description sd -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Us³ugi Bacula Storage sk³adaj± siê z programów obs³uguj±cych
przechowywanie danych oraz odzyskiwanie atrybutów i danych na
fizycznych no¶nikach lub wolumenach. Innymi s³owy, demon Storage jest
odpowiedzialny za odczyt i zapis ta¶m (lub innych no¶ników do
przechowywania danych, np. plików). Us³ugi Storage dzia³aj± jako demon
na maszynie, która zawiera urz±dzenie backupowe (zwykle napêd
ta¶mowy).

%package rescue
Summary:	Bacula - The Network Backup Solution
Summary(pl):	Bacula - rozwi±zanie do wykonywania kopii zapasowych po sieci
Group:		Networking/Utilities
Requires:	%{name}-fd = %{epoch}:%{version}-%{release}
Requires:	coreutils
Requires:	util-linux

%description rescue
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

This package installs scripts for disaster recovery and builds rescue
floppy disk for bare metal recovery. 

To make the bacula rescue disk run "./make_rescue_disk --copy-static-bacula
- --copy-etc-files" from the %{_sysconfdir}/rescue directory. To recreate the
rescue information for this system run ./getdiskinfo again.

%description rescue -l pl
Bacula - przychodzi noc± i wysysa ¿ywotny ekstrakt z komputerów.

Bacula to zbiór programów umo¿liwiaj±cych administratorowi na
zarz±dzanie kopiami zapasowymi, odzyskiwaniem i weryfikacj± danych
w sieci komputerów ró¿nego rodzaju. W terminologii technicznej jest to
program do kopii zapasowych pracuj±cy w architekturze klient-serwer.
Bacula jest stosunkowo ³atwa w u¿yciu i wydajna, oferuj±c przy tym
wiele zaawansowanych mo¿liwo¶ci przy zarz±dzaniu no¶nikami,
u³atwiaj±cych znalezienie i odzyskanie utraconych lub uszkodzonych
plików.

Ten pakiet zawiera skrypty do odtwarzania po awarii i tworzy dyskietkê
ratunkowe do odtwarzania systemu od zera. 

Aby stworzyæ dyskietkê ratunkow± Baculi, nale¿y uruchomiæ "./make_rescue_disk
--copy-static-bacula - --copy-etc-files" z katalogu
%{_sysconfdir}/rescue . Aby ponownie utworzyæ informacje ratunkowe dla
danego systemu, nale¿y ponownie uruchomiæ ./getdiskinfo .

%prep
%setup -q -a 1
sed -i -e 's#wx-config#wxgtk2-2.4-config#g' configure*
sed -i -e 's#-lreadline -ltermcap#-lreadline#g' configure*
sed -i -e 's#bindir=.*#bindir=%{_bindir}#g' \
	src/cats/create_* src/cats/delete_* src/cats/drop_* \
	src/cats/grant_* src/cats/make_* src/cats/update_*
sed -i -e 's/@hostname@/--hostname--/' src/*/*.conf.in

%build
cp -f %{_datadir}/automake/config.sub autoconf
CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/readline"
%configure \
	--with-scriptdir=%{_libexecdir}/%{name} \
	--enable-gnome \
	--disable-conio \
	--enable-smartalloc \
	--enable-wx-console \
	--enable-tray-monitor \
	--with-readline \
	--with-tcp-wrappers \
	--with-working-dir=%{_var}/lib/%{name} \
	--with-dump-email="root@localhost" \
	--with-job-email="root@localhost" \
	--with-smtp-host=localhost \
	--with-pid-dir=/var/run \
	--with-subsys-dir=/var/lock/subsys \
	--with-sqlite \
	--with-dir-password="#FAKE-dir-password#" \
	--with-fd-password="#FAKE-fd-password#" \
	--with-sd-password="#FAKE-sd-password#" \
	--with-mon-dir-password="#FAKE-mon-dir-password#" \
	--with-mon-fd-password="#FAKE-mon-fd-password#" \
	--with-mon-sd-password="#FAKE-mon-sd-password#" \
	--enable-static-fd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,pam.d,sysconfig}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_mandir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# static daemon
strip -R.comment -R.note src/filed/static-bacula-fd
install src/filed/static-bacula-fd $RPM_BUILD_ROOT%{_sysconfdir}/rescue/bacula-fd

# tray-monitor is for regular users
mv $RPM_BUILD_ROOT%{_sbindir}/bacula-tray-monitor $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-dir
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-fd
install %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-sd
install %{SOURCE13} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}-dir
install %{SOURCE14} $RPM_BUILD_ROOT/etc/sysconfig/bacula-dir
install %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/bacula-fd
install %{SOURCE16} $RPM_BUILD_ROOT/etc/sysconfig/bacula-sd

install scripts/bacula.png $RPM_BUILD_ROOT%{_pixmapsdir}/bacula.png
install src/tray-monitor/generic.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/bacula-tray-monitor.xpm
install scripts/bacula.desktop.gnome2 $RPM_BUILD_ROOT%{_desktopdir}/bacula.desktop
sed -e 's/gnome-console/wx-console/g;s/Console/Wx Console/g' \
	scripts/bacula.desktop.gnome2 > $RPM_BUILD_ROOT%{_desktopdir}/bacula-wx.desktop
sed -e 's#%{_sbindir}#%{_bindir}#' \
	scripts/bacula-tray-monitor.desktop > $RPM_BUILD_ROOT%{_desktopdir}/bacula-tray-monitor.desktop

# install the rescue stuff, these are the rescue scripts
install rescue/linux/floppy/backup.etc.list $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install rescue/linux/floppy/*_* $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install rescue/linux/floppy/getdiskinfo $RPM_BUILD_ROOT%{_sysconfdir}/rescue
install rescue/linux/floppy/sfdisk.bz2 $RPM_BUILD_ROOT%{_sysconfdir}/rescue

# install the updatedb scripts
install updatedb/update_sqlite* $RPM_BUILD_ROOT%{_libexecdir}/%{name}

# manual
cp -a man1 man8 $RPM_BUILD_ROOT%{_mandir}

install -d html-manual
cp -a doc/html-manual/*.{html,jpg,gif,css,png,txt} html-manual


# place for site passwords
touch $RPM_BUILD_ROOT%{_sysconfdir}/{dir-password,fd-password,sd-password}
touch $RPM_BUILD_ROOT%{_sysconfdir}/{mon-dir-password,mon-fd-password,mon-sd-password}

# some file changes
rm -f $RPM_BUILD_ROOT%{_libexecdir}/%{name}/{gconsole,startmysql,stopmysql,bacula,bconsole,fd}
rm -f $RPM_BUILD_ROOT%{_sbindir}/static-bacula-fd
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/gnome*
touch $RPM_BUILD_ROOT%{_sysconfdir}/.pw.sed

%clean
rm -rf $RPM_BUILD_ROOT

%pre common
if [ -n "`getgid bacula`" ]; then
	if [ "`getgid bacula`" != "136" ]; then
		echo "Error: group bacula doesn't have gid=136. Correct this before installing bacula." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 136 -r -f bacula
fi
if [ -n "`id -u bacula 2>/dev/null`" ]; then
	if [ "`id -u bacula`" != "136" ]; then
		echo "Error: user bacula doesn't have uid=136. Correct this before installing bacula." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 136 -r -d /var/lib/bacula -s /bin/false -c "Bacula User" -g bacula bacula 1>&2
fi

%post common
echo "Updating bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	if ! [ -s $f ] ; then
		openssl rand -base64 33 > $f
	fi
	p=`cat $f`
	for cf in *.conf *.conf.rpmnew ; do
		[ -f $cf ] && sed -i -e"s:#FAKE-$f#:$p:" "$cf" || :
	done
done
for cf in *.conf *.conf.rpmnew ; do
	[ -f $cf ] && sed -i -e"s:--hostname--:`hostname`:" "$cf" || :
done

%postun common
if [ "$1" = "0" ]; then
	%userremove bacula
	%groupremove bacula
fi

%post dir
umask 077
[ -s %{_localstatedir}/bacula.db ] && \
	DB_VER=`echo "select * from Version;" | \
	%{_bindir}/sqlite %{_localstatedir}/bacula.db | tail -n 1 2>/dev/null`
if [ -z "$DB_VER" ]; then
# grant privileges and create tables
	%{_libexecdir}/%{name}/grant_bacula_privileges > dev/null
	%{_libexecdir}/%{name}/create_bacula_database > dev/null
	%{_libexecdir}/%{name}/make_bacula_tables > dev/null
elif [ "$DB_VER" -lt "8" ]; then
	echo "Backing up bacula tables"
	echo ".dump" | sqlite %{_localstatedir}/bacula.db | bzip2 > %{_localstatedir}/bacula_backup.sql.bz2
	type=sqlite
	echo "Upgrading bacula tables"
	if [ "$DB_VER" -lt "7" ]; then
		if [ "$DB_VER" -lt "6" ]; then
			if [ "$DB_VER" -lt "5" ]; then
				%{_libexecdir}/%{name}/update_${type}_tables_4_to_5
			fi
			%{_libexecdir}/%{name}/update_${type}_tables_5_to_6
		fi
		%{_libexecdir}/%{name}/update_${type}_tables_6_to_7
	fi
	%{_libexecdir}/%{name}/update_bacula_tables
	echo "If bacula works correctly you can remove the backup file %{_localstatedir}/bacula_backup.sql.bz2"
fi
chown -R bacula:bacula %{_localstatedir}
chmod -R u+rX,go-rwx %{_localstatedir}/*

echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

/sbin/chkconfig --add bacula-dir
if [ -f /var/lock/subsys/bacula-dir ]; then
	/etc/rc.d/init.d/bacula-dir restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/bacula-dir start\" to start Bacula Director daemon."
fi

%preun dir
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/bacula-dir ]; then
		/etc/rc.d/init.d/bacula-dir stop 1>&2
	fi
	/sbin/chkconfig --del bacula-dir
fi

%post fd
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

/sbin/chkconfig --add bacula-fd
if [ -f /var/lock/subsys/bacula-fd ]; then
	/etc/rc.d/init.d/bacula-fd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/bacula-fd start\" to start Bacula File daemon."
fi

%preun fd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/bacula-fd ]; then
		/etc/rc.d/init.d/bacula-fd stop 1>&2
	fi
	/sbin/chkconfig --del bacula-fd
fi

%post sd
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

/sbin/chkconfig --add bacula-sd
if [ -f /var/lock/subsys/bacula-sd ]; then
	/etc/rc.d/init.d/bacula-sd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/bacula-sd start\" to start Bacula Storage daemon."
fi

%preun sd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/bacula-sd ]; then
		/etc/rc.d/init.d/bacula-sd stop 1>&2
	fi
	/sbin/chkconfig --del bacula-sd
fi

%pre console
if [ -e %{_sysconfdir}/console.conf -a ! -e %{_sysconfdir}/bconsole.conf ]; then
	mv %{_sysconfdir}/console.conf %{_sysconfdir}/bconsole.conf
fi

%post console
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

%post console-wx
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

%post console-gnome
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

%post tray-monitor
echo "Updating Bacula passwords and names..."
cd /etc/bacula
for f in *-password ; do
	p=`cat $f`
	sed -i -e"s:#FAKE-$f#:$p:" *.conf *.conf.rpmnew
done
sed -i -e"s:--hostname--:`hostname`:" *.conf *.conf.rpmnew

%post rescue
# link our current installed conf file to the rescue directory
ln -sf %{_sysconfdir}/bacula-fd.conf %{_sysconfdir}/rescue/bacula-fd.conf

# run getdiskinfo
echo "Creating rescue files for this system..."
cd %{_sysconfdir}/rescue
./getdiskinfo

%preun rescue
# remove the files created after the initial rpm installation
if [ "$1" = "0" ]; then
	rm -f %{_sysconfdir}/rescue/bacula-fd.conf
	rm -f %{_sysconfdir}/rescue/partition.*
	rm -f %{_sysconfdir}/rescue/format.*
	rm -f %{_sysconfdir}/rescue/mount_drives
	rm -f %{_sysconfdir}/rescue/start_network
	rm -f %{_sysconfdir}/rescue/sfdisk
	rm -rf %{_sysconfdir}/rescue/diskinfo/*
fi

%files common
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/*-password
%attr(755,root,root) %{_sbindir}/btraceback
%attr(755,root,root) %{_sbindir}/bsmtp
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/btraceback.gdb
%attr(770,root,bacula) %dir %{_localstatedir}

%files dir
%defattr(644,root,root,755)
%doc ChangeLog CheckList ReleaseNotes kernstodo LICENSE
%doc doc/*.pdf html-manual examples
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-dir.conf
%ghost %{_sysconfdir}/.pw.sed
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/bacula-dir
%attr(754,root,root) /etc/rc.d/init.d/bacula-dir
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/bacula-dir
%attr(755,root,root) %{_sbindir}/bacula-dir
%attr(755,root,root) %{_sbindir}/dbcheck
%{_mandir}/man8/bacula-dir.8*
%{_mandir}/man1/dbcheck.1*
%{_libexecdir}/%{name}/query.sql
%attr(755,root,root) %{_libexecdir}/%{name}/create_sqlite_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_sqlite_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_sqlite_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_sqlite_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_sqlite_tables*
%attr(755,root,root) %{_libexecdir}/%{name}/create_bacula_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_bacula_database
%attr(755,root,root) %{_libexecdir}/%{name}/drop_bacula_tables
%attr(755,root,root) %{_libexecdir}/%{name}/grant_bacula_privileges
%attr(755,root,root) %{_libexecdir}/%{name}/make_bacula_tables
%attr(755,root,root) %{_libexecdir}/%{name}/update_bacula_tables
%attr(755,root,root) %{_libexecdir}/%{name}/make_catalog_backup
%attr(755,root,root) %{_libexecdir}/%{name}/delete_catalog_backup

%files fd
%defattr(644,root,root,755)
%doc LICENSE
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-fd.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-fd
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/bacula-fd
%attr(755,root,root) %{_sbindir}/bacula-fd
%{_mandir}/man8/bacula-fd.8*

%files sd
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-sd.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-sd
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/bacula-sd
%attr(755,root,root) %{_sbindir}/bacula-sd
%attr(755,root,root) %{_sbindir}/bcopy
%attr(755,root,root) %{_sbindir}/bextract
%attr(755,root,root) %{_sbindir}/bls
%attr(755,root,root) %{_sbindir}/bscan
%attr(755,root,root) %{_sbindir}/btape
%{_libexecdir}/%{name}/mtx-changer
%{_mandir}/man8/bacula-sd.8*
%{_mandir}/man1/bcopy.1*
%{_mandir}/man1/bextract.1*
%{_mandir}/man1/bls.1*
%{_mandir}/man1/bscan.1*
%{_mandir}/man1/btape.1*

%files console
%defattr(644,root,root,755)
%doc LICENSE
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bconsole.conf
%attr(755,root,root) %{_sbindir}/bconsole
%{_mandir}/man1/bconsole.1*

%files console-wx
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/bacula-wx.desktop
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/wx-console.conf
%attr(755,root,root) %{_sbindir}/wx-console
%{_mandir}/man1/wx-console.1*

%files console-gnome
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/bacula.desktop
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/gnome-console.conf
%attr(755,root,root) %{_sbindir}/gnome-console
#%{_mandir}/man1/gnome-console.1*

%files tray-monitor
%defattr(644,root,root,755)
%doc LICENSE
%{_pixmapsdir}/%{name}-tray-monitor.xpm
%{_desktopdir}/%{name}-tray-monitor.desktop
%attr(644,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/tray-monitor.conf
%attr(755,root,root) %{_bindir}/bacula-tray-monitor
#%{_mandir}/man1/bacula-tray-monitor.1*

%files rescue
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_sysconfdir}/rescue
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/backup.etc.list
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/bacula-fd
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/format_floppy
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/getdiskinfo
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/make_rescue_disk
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/restore_bacula
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/restore_etc
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/run_grub
%attr(755,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/run_lilo
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/rescue/sfdisk.bz2
