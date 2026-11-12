"""Felles oppsett for bygget og henteskriptene: hvilken base de skriver til, og kildelistene.

Standard er dette repoet. Med miljøvariabelen REGELVERK_ROT kan verktøyet kjøres mot en annen
regelverksbase, for eksempel en mappe i et annet repo som har sin egen regelverk.json:

    REGELVERK_ROT=/sti/til/base python3 verktoy/bygg.py

Kildelistene som ellers står i skriptene (direktoratenes nettsider, Navs hovednummer og andre navn
lovene omtales med), leses fra tolkningskilder.json i basen når den fila finnes. Da gjelder bare
listene i fila, ikke standardlistene i skriptene. Se tolkningskilder.eksempel.json.
"""
import json
import os
from pathlib import Path

ROT = Path(os.environ.get("REGELVERK_ROT") or Path(__file__).resolve().parent.parent).resolve()
TOLKNINGSKILDER_FIL = ROT / "tolkningskilder.json"


def liste(navn: str, standard):
    """Listen `navn` fra tolkningskilder.json i basen hvis fila finnes, ellers `standard`."""
    if not TOLKNINGSKILDER_FIL.exists():
        return standard
    return json.loads(TOLKNINGSKILDER_FIL.read_text(encoding="utf-8")).get(navn, type(standard)())


def lovsett(navn: str, lover) -> tuple:
    """Hvilke lover som er kommet til siden forrige kjøring av henteskriptet `navn`.

    Returnerer (nye lover, funksjon som lagrer dagens sett). Kall lagre-funksjonen etter at statusfila
    er skrevet. Første gang fila mangler, regnes ingen lover som nye (alt hentes uansett første gang).
    """
    fil = ROT / "regelverk" / f"{navn}-lover.txt"
    dagens = sorted(set(lover))
    forrige = set(fil.read_text(encoding="utf-8").split()) if fil.exists() else set(dagens)

    def lagre():
        fil.parent.mkdir(parents=True, exist_ok=True)
        fil.write_text("\n".join(dagens) + "\n", encoding="utf-8")

    return set(dagens) - forrige, lagre
