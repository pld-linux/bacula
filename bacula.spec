# TODO:
# - files section
# - rpm scripts
#
Summary:	Bacula - The Network Backup Solution
Name:		bacula
Version:	1.34.6
Release:	0.1
Group:		Networking/Utilities
License:	GPL v2
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	9de593cb206df126a8e27774281c5bf6
Source1:	http://www.tux.org/pub/distributions/tinylinux/tomsrtbt/tomsrtbt-2.0.103.tar.gz
# Source1-md5:	d5ee50efb28986d564547d5da5de2483
Source2:	%{name}-dir.init
Source3:	%{name}-fd.init
Source4:	%{name}-sd.init
Source5:	%{name}.logrotate
URL:		http://www.bacula.org/
BuildRequires:	mtx
BuildRequires:	wxGTK2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	sqlite2-devel
BuildRequires:	libwrap-devel
BuildRequires:	zlib-devel
BuildRequires:	acl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glibc-static
BuildRequires:	acl-static
BuildRequires:	libwrap-static
BuildRequires:	libstdc++-static
Provides:	bacula-dir
Provides:	bacula-sd
Provides:	bacula-fd
Provides:	bacula-server
Conflicts:	bacula-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

%package client
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Provides:	bacula-fd

%description client
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This is the File daemon (Client) only package. It includes the command
line console program.

%package rescue

Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Requires:	coreutils
Requires:	util-linux
Requires:	libc5
Requires:	bacula-fd

%description rescue
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This package installs scripts for disaster recovery and builds rescue
floppy disks for bare metal recovery. This package includes tomsrtbt
(http://www.toms.net/rb/, by Tom Oehser, Tom@Toms.NET) to provide a
tool to build a boot floppy disk.

To create a boot disk run "./getdiskinfo" from the
%{_sysconfdir}/rescue directory (this is done when the package is
first installed), then run "./install.s" from the
%{_sysconfdir}/rescue/tomsrtbt/ directory. To make the bacula rescue
disk run "./make_rescue_disk --copy-static-bacula
- --copy-etc-files" from the %{_sysconfdir}/rescue directory. To
  recreate the rescue information for this system run ./getdiskinfo
  again.

%package updatedb
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities

%description updatedb
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This package installs scripts for updating older versions of the
bacula database.

%package wxconsole
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Requires:	bacula-fd

%description wxconsole
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This is the WX Console package. It is an add-on to the client or
server packages.

%prep
%setup -q -a 1
sed -i -e 's#wx-config#wxgtk2-2.4-config#g' configure*
sed -i -e 's#-lreadline -ltermcap#-lreadline#g' configure*

%build
# patches for the bundled sqlite scripts
# patch the make_sqlite_tables script for installation bindir
patch src/cats/make_sqlite_tables.in src/cats/make_sqlite_tables.in.patch
# patch the create_sqlite_database script for installation bindir
patch src/cats/create_sqlite_database.in src/cats/create_sqlite_database.in.patch
# patch the make_catalog_backup script for installation bindir
patch src/cats/make_catalog_backup.in src/cats/make_catalog_backup.in.patch
# patch the update_sqlite_tables script for installation bindir
patch src/cats/update_sqlite_tables.in src/cats/update_sqlite_tables.in.patch

CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/readline"
%configure \
	--disable-gnome \
	--disable-conio \
	--enable-wx-console \
	--with-readline \
	--with-tcp-wrappers \
	--with-working-dir=%{_var}/lib/%{name} \
	--with-dump-email="root@localhost" \
	--with-job-email="root@localhost" \
	--with-smtp-host=localhost \
	--with-pid-dir=/var/run \
	--with-subsys-dir=/var/lock/subsys \
	--with-sqlite \
	--enable-static-fd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,pam.d,security/console.apps}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rescue/tomsrtbt,updatedb}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# static daemon
strip src/filed/static-bacula-fd
install src/filed/static-bacula-fd $RPM_BUILD_ROOT%{_sysconfdir}/rescue/bacula-fd

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-dir
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-fd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-sd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

install scripts/bacula.png $RPM_BUILD_ROOT%{_pixmapsdir}/bacula.png

# install the rescue stuff, these are the rescue scripts
install rescue/linux/backup.etc.list $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/format_floppy $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/getdiskinfo $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/make_rescue_disk $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/restore_bacula $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/restore_etc $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/run_grub $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/run_lilo $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/sfdisk.bz2 $RPM_BUILD_ROOT%{_sysconfdir}/rescue/

# this is the tom's root boot disk
install tomsrtbt-*/* $RPM_BUILD_ROOT%{_sysconfdir}/rescue/tomsrtbt/

# install the updatedb scripts
install updatedb/* $RPM_BUILD_ROOT%{_sysconfdir}/updatedb/

# manual
install -d html-manual
cp -a doc/html-manual/*.{html,jpg,gif,css} html-manual/

# drop some files
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/{gconsole,startmysql,stopmysql}

%pre
# test for bacula database older than version 6
if [ -s %{_var}/lib/%{name}/bacula.db ];then
	DB_VER=`echo "select * from Version;" | %{_bindir}/sqlite %{_var}/lib/%{name}/bacula.db | tail -n 1 2>/dev/null`
	if [ -n "$DB_VER" ] && [ "$DB_VER" -lt "6" ]; then
		echo "This bacula upgrade will update a bacula database from version 6 to 7."
		echo "You appear to be running database version $DB_VER. You must first update"
		echo "your database to version 6 and then install this upgrade. The alternative"
		echo "is to use %{_sysconfdir}/drop_sqlite_tables to delete all your your current"
		echo "catalog information, then do the upgrade. Information on updating a"
		echo "database older than version 6 can be found in the release notes."
		exit 1
	fi
fi
# check for and copy %{_sysconfdir}/console.conf to bconsole.conf
if [ -s %{_sysconfdir}/console.conf ];then
	cp -a %{_sysconfdir}/console.conf %{_sysconfdir}/bconsole.conf
fi

%post
# add our links
if [ "$1" -ge 1 ] ; then
	/sbin/chkconfig --add bacula-dir
	/sbin/chkconfig --add bacula-fd
	/sbin/chkconfig --add bacula-sd
fi

# test for an existing database
if [ -s %{_var}/lib/%{name}/bacula.db ]; then
	DB_VER=`echo "select * from Version;" | %{_bindir}/sqlite %{_var}/lib/%{name}/bacula.db | tail -n 1 2>/dev/null`
	# check to see if we need to upgrade a 1.32 or lower database
	if [ "$DB_VER" -lt "7" ]; then
		echo "This release requires an upgrade to your bacula database."
		echo "Backing up your current database..."
		echo ".dump" | %{_bindir}/sqlite %{_var}/lib/%{name}/bacula.db | bzip2 > %{_var}/lib/%{name}/bacula_backup.sql.bz2
		echo "Upgrading bacula database ..."
		%{_sysconfdir}/update_sqlite_tables
		echo "If bacula works correctly you can remove the backup file %{_var}/lib/%{name}/bacula_backup.sql.bz2"
	fi
else
	# create the database and tables
	echo "Hmm, doesn't look like you have an existing database."
	echo "Creating SQLite database..."
	%{_sysconfdir}/create_sqlite_database
	echo "Creating the SQLite tables..."
	%{_sysconfdir}/make_sqlite_tables
fi

%preun
# delete our links
if [ $1 = 0 ]; then
	/sbin/chkconfig --del bacula-dir
	/sbin/chkconfig --del bacula-fd
	/sbin/chkconfig --del bacula-sd
fi

%post client
# add our link
if [ "$1" -ge 1 ] ; then
	/sbin/chkconfig --add bacula-fd
fi

%preun client
# delete our link
if [ $1 = 0 ]; then
	/sbin/chkconfig --del bacula-fd
fi

%post updatedb
echo "The database update scripts were installed to %{_sysconfdir}/updatedb"

%clean
rm -rf $RPM_BUILD_ROOT

%post rescue
# link our current installed conf file to the rescue directory
ln -s %{_sysconfdir}/bacula-fd.conf %{_sysconfdir}/rescue/bacula-fd.conf

# run getdiskinfo
echo "Creating rescue files for this system..."
cd %{_sysconfdir}/rescue
./getdiskinfo

%preun rescue
# remove the files created after the initial rpm installation
rm -f %{_sysconfdir}/rescue/bacula-fd.conf
rm -f %{_sysconfdir}/rescue/partition.*
rm -f %{_sysconfdir}/rescue/format.*
rm -f %{_sysconfdir}/rescue/mount_drives
rm -f %{_sysconfdir}/rescue/start_network
rm -f %{_sysconfdir}/rescue/sfdisk
rm -rf %{_sysconfdir}/rescue/diskinfo/*

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog ReleaseNotes VERIFYING kernstodo doc/bacula.pdf html-manual
%attr(755,root,root) %{_sbindir}/bacula-dir
%attr(755,root,root) %{_sbindir}/bacula-fd
%attr(755,root,root) %{_sbindir}/bacula-sd
%attr(755,root,root) %{_sbindir}/bcopy
%attr(755,root,root) %{_sbindir}/bextract
%attr(755,root,root) %{_sbindir}/bls
%attr(755,root,root) %{_sbindir}/bscan
%attr(755,root,root) %{_sbindir}/btape
%attr(755,root,root) %{_sbindir}/btraceback
%attr(755,root,root) %{_sbindir}/bconsole
%attr(755,root,root) %{_sbindir}/dbcheck
%attr(755,root,root) %{_sbindir}/bsmtp
%attr(755,root,root) %{_sbindir}/static-bacula-fd
%dir %{_sysconfdir}
%{_sysconfdir}/bacula
%{_sysconfdir}/bconsole
%{_sysconfdir}/fd
%{_sysconfdir}/create_bacula_database
%{_sysconfdir}/drop_bacula_database
%{_sysconfdir}/grant_bacula_privileges
%{_sysconfdir}/make_bacula_tables
%{_sysconfdir}/drop_bacula_tables
%{_sysconfdir}/update_bacula_tables
%{_sysconfdir}/create_sqlite_database
%{_sysconfdir}/drop_sqlite_database
%{_sysconfdir}/grant_sqlite_privileges
%{_sysconfdir}/make_sqlite_tables
%{_sysconfdir}/drop_sqlite_tables
%{_sysconfdir}/update_sqlite_tables
%{_sysconfdir}/make_catalog_backup
%{_sysconfdir}/delete_catalog_backup
%{_sysconfdir}/mtx-changer
%{_sysconfdir}/query.sql
%{_sysconfdir}/btraceback.gdb
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-dir.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-fd.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-sd.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bconsole.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-dir
%attr(754,root,root) /etc/rc.d/init.d/bacula-fd
%attr(754,root,root) /etc/rc.d/init.d/bacula-sd
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/bacula
%dir %{_var}/lib/%{name}

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/bacula-fd
%attr(755,root,root) %{_sbindir}/btraceback
%attr(755,root,root) %{_sbindir}/bsmtp
%attr(755,root,root) %{_sbindir}/bconsole
%{_sysconfdir}/fd
%{_sysconfdir}/bconsole
%{_sysconfdir}/btraceback.gdb
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bacula-fd.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bconsole.conf
%attr(754,root,root) /etc/rc.d/init.d/bacula-fd
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/bacula
%dir %{_var}/lib/%{name}

%files rescue
%defattr(644,root,root,755)
%{_sysconfdir}/rescue

%files updatedb
%defattr(644,root,root,755)
%{_sysconfdir}/updatedb

%files wxconsole
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/wx-console
%config(noreplace) %{_sysconfdir}/wx-console.conf
%{_pixmapsdir}/bacula.png
