import json
import os
import subprocess

import pandas as pd

index = pd.read_csv("info.csv")
basedir = os.getcwd()

for i, row in index.iterrows():
    bicho = row["bicho"]
    marker = row["marker"]
    # Prepapar barque
    # Ejecutar prepare.sh
    result_preparar_config = subprocess.run(
        ["sh", "preparar_config.sh", str(marker)], env=os.environ
    )
    nuevodir = f"./{marker}/barque"
    os.chdir(nuevodir)
    # descargar todos los accessions
    result_descarga = subprocess.run(
        [
            "sh",
            f"descargar_multiple.sh",
            f"14_tests/{marker}/{marker}_accessions.txt",
            f"04_data",
        ],
        env=os.environ,
    )
    print(result_descarga)
    # rename
    result_rename = subprocess.run(
        [
            "python",
            f"rename_script.py",
            f"04_data",
            str(bicho),
        ],
        env=os.environ,
    )
    # arrancar barque
    result_barque = subprocess.run(
        [
            "bash",
            f"barque",
            f"02_info/barque_config.sh",
        ],
        env=os.environ,
    )

    os.chdir(basedir)

    # zipear 12_results y 99_logs
    result_cleanup = subprocess.run(
        ["sh", "cleanup.sh", str(marker)],
        env=os.environ,
        capture_output=True,
        text=True,
        check=True,
    )
    checksums = json.loads(result_cleanup.stdout)
    results_checksum = checksums["results_checksum"]
    logfiles_checksum = checksums["logfiles_checksum"]

    index.loc[i, "results_checksum"] = results_checksum
    index.loc[i, "logfiles_checksum"] = logfiles_checksum
print(index)  # printear tabla
index.to_csv("output.csv", index=False, header=True)
