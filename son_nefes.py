#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmuş kapısı kapanmadan önceki son nefes.

Çalışır. Bağımlılık istemez. Patates istemez.
Çıkış kodu = kaldırımda kalan yolcu (0-125).
"""

from __future__ import annotations

import argparse
import random
import sys
import time

BAHANELER = [
    "abi bir kişilik yer var mı, çocuk okulda",
    "kartım içeride kaldı, kapıyı yarım santim aç",
    "ben inecektim aslında ama kapı beni içeri aldı",
    "şoför bey bir durak, yemin ederim bir durak",
    "çantam kaldırımda, çanta da yolcu sayılır mı",
    "arkadaşım yetişiyor, görüyor musun, o koşan nokta",
    "ben zaten ayaktayım, ayakta yer kaplamam teori gereği",
]

RUHLAR = [
    ("merhametli", 0.55),
    ("nötr", 0.25),
    ("kapı filozofu", 0.05),
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Kapı kapanmadan önceki son 4 saniyeyi resmi ciddiyetle simüle eder."
    )
    p.add_argument("--yolcu", type=int, default=7, help="kaldırımdaki aday sayısı")
    p.add_argument("--hiz", type=float, default=0.35, help="saniye cinsinden dram hızı")
    p.add_argument(
        "--protokol",
        choices=["sokak", "resmi"],
        default="sokak",
        help="resmi protokol daha az gülümser",
    )
    p.add_argument("--tohum", type=int, default=None, help="aynı kapıyı tekrar kapatmak için")
    return p.parse_args()


def binen_sayisi(aday: int, ruh: str) -> int:
    if aday <= 0:
        return 0
    tavan = {"merhametli": 3, "nötr": 1, "kapı filozofu": 0}[ruh]
    return min(aday, random.randint(0, tavan))


def main() -> int:
    args = parse_args()
    if args.tohum is not None:
        random.seed(args.tohum)
    aday = max(0, args.yolcu)
    ruh, _ = random.choice(RUHLAR)
    print("DOLMUŞ KAPISI KAPANMADAN SON NEFES")
    print("protokol:", args.protokol, "| şoför ruhu:", ruh)
    print("kaldırım adayı:", aday)
    print("-" * 42)
    for saniye in (4, 3, 2, 1):
        bahane = random.choice(BAHANELER)
        print(f"[{saniye}] {bahane}")
        time.sleep(max(0.0, args.hiz))
    binen = binen_sayisi(aday, ruh)
    if args.protokol == "resmi" and binen > 0:
        binen = max(0, binen - 1)
        print("resmi protokol: bir kişi evraka takıldı, inmedi sayıldı.")
    kalan = aday - binen
    print("-" * 42)
    print("KAPI.")
    print(f"binen: {binen} | kaldırımda kalan: {kalan}")
    if kalan == 0:
        print("mucize. loglara yazıldı. kimse inanmayacak.")
    else:
        print("son nefes kaldırıma düştü. sonraki dolmuş da böyle.")
    return min(kalan, 125)


if __name__ == "__main__":
    sys.exit(main())
