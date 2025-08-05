# ms2-tb1-cakrai17-13224008
Sederhananya, node ini merupakan perantara dari node twist_command_randomizer dengan movement_reader. Node ini merupakan subscriber dari topic autonomous_vel, kemudian ia mempublish data olahan sebelumnya ke topic cmd_type dan cmd_vel. Node ini masih belum sempurna dan boleh dibilang masih salah. Hal ini berdasarkan output dari node ini yang menunjukkan error dan tidak menampilkan data translasi maupun rotasi secara random.

Panduan dalam menggunakan Node:
1) Buat workspace yang nantinya digunakan untuk menjalankan node
2) Clone repo https://github.com/garudago/ms2-tubes1-cakrai17.git ke dalam folder ‘src’ pada workspace Anda.
3) Clone repo ini ke dalam folder 'src' pada workspace Anda.
4) Masuk ke direktori package pkg_13224008 yang di dalam foldernya berisi node autonomous_cmd_bridge.
5) Setelah masuk, beri izin ke file autonomous_cmd_bridge.py agar dapat dijalankan dengan memasukkan kode "chmod +x autonomous_cmd_bridge.py". Pastikan Anda telah berada di dalam direktori autonomous_cmd_bridge.
6) Kemudian, kembali ke direktori workspace. Lakukan sourcing pada workspace tersebut dengan memasukkan kode
"source /opt/ros/humble/setup.bash"
"source install/setup.bash"
7) Lakukan colcon build
    "colcon build --symlink-install"
8) Jalankan node
    "ros2 run pkg_13224008 autonomous_cmd_bridge.py"
9) Buka terminal baru dan jalankan node yang berasal dari package magang 2025 dengan prosedur awal yang sama.
10) Jalankan node tersebut
    "ros2 launch magang_2025 milestone2.launch.py"