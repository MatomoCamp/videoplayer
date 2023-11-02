from string import ascii_lowercase, digits

chat_rooms = {
    "3TTRKG": "spa-applications",
    "7AJEKD": "background-tracking",
    "8HSWJD": "q-a",
    "9JHC8H": "closing-event",
    "DM8S7W": "matomo-for-a-saas",
    "ENHZCR": "gdpr-compliance",
    "FDEE9Z": "research-trial",
    "G8K8AV": "incidences-cote-infra",
    "G98E3P": "user-feedback-plugin",
    "GDGZXF": "event-introduction",
    "GF7XD9": "tagmanager-basics",
    "GMUXZZ": "conversion-rate-optimization",
    "GR9YQZ": "matomo-kompakt",
    "HU8NSN": "risk-for-a-dpo",
    # "KDBDPX": "translating-matomo",
    "LKVJQ8": "public-sector",
    "LZ8NYG": "compliant-with-privacy-regulations",
    "M9XPRG": "cleaninsights-talk",
    "MKKVHX": "building-own-business",
    "N3U3BT": "metabase",
    "PBWV7L": "seo",
    "PX7EHX": "configurer-matomo-dans-le-respect-du-rgpd",
    "QRSQ8D": "break-and-fix",
    "URWXGR": "millions-of-pageviews",
    "WGWW8R": "surveillance-societies",
    # "XAAHDQ": "open-source-data-visualization",
    "XTF7GX": "tips-and-tricks",
    "Y9AAMG": "host-own-instance",
    "ZBWZHJ": "cleaninsights-workshop",
    "QQJ3ZS": "privacy-in-web-analytics",

    # 2022

    "H7YHTG": "event-introduction-2022",
    "JSPF8U": "multi-server-and-docker",
    "PYQY3A": "monter-une-infrastructure-matomo",
    "3DBQCM": "developing-a-plugin",
    "3LRN3P": "ideal-matomo",
    "EMG79M": "reussir-limplementation-de-matomo",
    "MWQUT7": "future-of-matomo",
    "S37GBU": "gestion-de-projet-web-analytics",
    "PU7SJR": "contributing-back",
    "33QBWR": "importance-of-privacy",
    "AXGTWL": "analysez-vos-performances",
    "SXLAJL": "matomo-in-a-data-stack",
    "R393MD": "external-dashboards-data-visualization",
    "SNEUXP": "migration-de-vos-datas-ga-vers-matomo",
    "QCGUJB": "security-hardening",
    "ADJLAW": "dashboards-with-apache-superset",
    "PYT37H": "matomo-et-wordpress",
    "QB8VY8": "using-kubernetes-and-docker",
    "XGPBTU": "matomo-and-us-distributors",
    "XMGR83": "les-traductions-dans-matomo",
    "UKTQD8": "matomo-su-kubernetes",
    "EDHADW": "tag-manager-and-consent-solutions",
    "CQ3TRP": "vanilla-analytics",
    "U9GDMC": "vuejs-in-plugins",
    "TPFDWN": "dashboard",
    "SRDLAJ": "das-problem-zu-viel",
    "KDWXFH": "intranet-analytics",
    "XRVPDS": "das-problem-zu-wenig",
    "ZXGJYA": "improve-seo",
    "7YDHL7": "tracking-spas",
    "97RZGZ": "standortermittlung",
    "FXLH93": "snowplow",
    "FUD7JR": "log-analytics",
    "BRH8SH": "datenschutzkonformes-performance-marketing",
    "N3WJCA": "creating-plugins-as-non-developers",
    "YE9MYB": "plausible-analytics",
    "389UYH": "joomla",
    "E893JM": "web-analytics-book",
    "WXXXXE": "migrating-matomo",
    "ST38HK": "closing-event-2022",

    #2023

    "NQLKF8": "event-introduction-2023",
    "38BMH9": "data-privacy-framework",
    "WCKGVN": "privacy-et-consentement",
    "UPVEX9": "ghost-cms",
    "3C8Q7N": "analysez-vos-donnees",
    "MR7XAA": "surveys-plugin",
    "ZQYENT": "tips-and-tricks-for-marketers",
    # "ALJTKA": "Comment gérer 1000 sites, des dizaines de serveurs Matomo et +100 utilisateurs à travers une seule plateforme ?",
    "NBXLRD": "forms-use-cases",
    "9SWQLW": "raw-data-to-tableau",
    "TFFTV3": "advanced-dashboarding",
    "PWSJSQ": "plugin-best-practices",
    "JX37F9": "ai-act",
    "AMSSFM": "mastering-troubleshooting",
    "8SGMFE": "supervision-dusage-de-site",
    "MPC7TK": "tag-manager-best-practices",
    "CBLEVN": "retrieving-api-data-using-ai",
    "3ZYJKG": "les-solutions-analytiques-pour-les-entreprises-francaises",
    "C7FZYR": "advanced-data-visualization-with-apache-superset",
    "S8VPGQ": "interactive-online-events-with-workadventure",
    "7C7LKL": "b2b-markkinointiapua",
    "NZZNJN": "matomo-servers-management",
    "RTBNWR": "matomo-unleashed",
    "GUNNPK": "erste-schritte",
    "CWQPAA": "e-commerce-tracking",
    "3XRSQM": "insights-fur-optimierung",
    "ZCJUUS": "new-zealands-digital-analytics-landscape",
    "MME8MC": "privacy-through-clean-insights",
    "T9E8EG": "creating-a-theme",
    "7AJ39H": "plugin-development-competition",
    "ZDHAQF": "website-conversions-for-smaller-manufacturers",
    "RJAS9R": "measure-your-users-weather",
    "8Z3ZUJ": "virtual-pageviews",
    "B9SPEP": "bigquery-and-looker",
    "RTLKVY": "matomo-on-sharepoint",
    "G8NL87": "kampagnen-tracking",
    "9F9DFT": "optimizing-intranet-success",
    "RJSXCB": "closing-event-2023",


}

archive_names = {
    "3TTRKG": "trackingSPA",
    "7AJEKD": "Background Tracking",
    "8HSWJD": "Q&A",
    "9JHC8H": "Closing",
    "DM8S7W": "SAAS",
    "ENHZCR": "GDPR Masses",
    "FDEE9Z": "Wrapped",
    "G8K8AV": "incidences côté infra",
    "G98E3P": "User Feedback",
    "GDGZXF": "Opening",
    "GF7XD9": "Tag Manager Basics",
    "GMUXZZ": "Conversion rate",
    "GR9YQZ": "Matomo Kompakt",
    "HU8NSN": "DPO",
    # "KDBDPX": "translating-matomo",
    "LKVJQ8": "Public Sector",
    "LZ8NYG": "Stay Compliant",
    "M9XPRG": "Cleaninsights",
    "MKKVHX": "Business",
    "N3U3BT": "Metabase",
    "PBWV7L": "SEO",
    "PX7EHX": "configurer RGPD",
    "QRSQ8D": "Break Matomo",
    "URWXGR": "Million Pageviews",
    "WGWW8R": "Surveillance Societies",
    # "XAAHDQ": "open-source-data-visualization",
    "XTF7GX": "Tips and Tricks",
    "Y9AAMG": "Host your own Instance",
    # "ZBWZHJ": "cleaninsights-workshop",
    "QQJ3ZS": "PII",

    "UKTQD8": "Matomo su Kubernetes",
    "H7YHTG": "Opening",
                            "JSPF8U": "Multi-Server and Docker",
    # "PYQY3A": "monter-une-infrastructure-matomo",
    "3DBQCM": "Your own plugin",
    "3LRN3P": "Ideal Matomo",
    "EMG79M": "Réussir l'implémentation de Matomo",
    "MWQUT7": "Future of Matomo",
    # "S37GBU": "gestion-de-projet-web-analytics",
    # "PU7SJR": "contributing-back",
    "33QBWR": "Importance of Privacy",
    # "AXGTWL": "analysez-vos-performances",
    # "SXLAJL": "matomo-in-a-data-stack",
    "R393MD": "External Dashboards & Data Visualization",
    # "SNEUXP": "migration-de-vos-datas-ga-vers-matomo",
    "QCGUJB": "Security Hardening",
    # "ADJLAW": "dashboards-with-apache-superset",
    # "PYT37H": "matomo-et-wordpress",
    # "QB8VY8": "using-kubernetes-and-docker",
    "XGPBTU": "Matomo and US Distributors",
    # "XMGR83": "les-traductions-dans-matomo",
    # "UKTQD8": "matomo-su-kubernetes",
    "EDHADW": "Tag Manager and Consent solutions",
    # "CQ3TRP": "vanilla-analytics",
    "U9GDMC": "VueJS in plugins",
    "TPFDWN": "Kick-ass dashboard",
    "SRDLAJ": "Das Problem \"zu viel\"",
    "KDWXFH": "Intranet Analytics",
    # "XRVPDS": "das-problem-zu-wenig",
    "ZXGJYA": "Improve your SEO",
    # "7YDHL7": "tracking-spas",
    "97RZGZ": "Standortermittlung",
    "FXLH93": "Snowplow",
    "FUD7JR": "Log Analytics",
    "BRH8SH": "Performance Marketing",
    "N3WJCA": "Creating plugins as non-developers",
    "YE9MYB": "Plausible Analytics",
    # "389UYH": "joomla",
    "E893JM": "Web Analytics Book",
    "WXXXXE": "Migrating Matomo",
    "ST38HK": "Closing",

}

workshop_urls = {
    "PBWV7L": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-4x6-d69-3j3",
    "GR9YQZ": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-utm-dis-kbn",
    "ZBWZHJ": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-y8m-nzp-x8r",
    "Y9AAMG": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-s3t-fj8-yt3",
}

recording_ids = {
    "G8K8AV": "hvT8uffTv5VUHuTBmKpTSw",
    "M9XPRG": "diyX79F4BuZK8211mw2fDK",
    "XTF7GX": "pzcpV32ibe7ersq663xHWu",
    "FDEE9Z": "dM3Rr4VNd2wvrA1EqyFc9T",
    "PBWV7L": "oiMkGGpP3mDNsJNL9d835B",
    "LKVJQ8": "8jEpE55dohwRHsQwPr5p6b",
    "DM8S7W": "oHbeE3zkk625HUvDVDtiVN",
    "LZ8NYG": "mmcu1wTvNLThuLti46Awza",
    "WGWW8R": "7jLhv438Q5vynKVMZ8ZqNb",
    "GDGZXF": "aeDEypqe36V3rit3zZ87k9",
    "9JHC8H": "nFQJq2ebTNQjeDCUTtEJo5",
    "GR9YQZ": "gqEzAyzDJz4KLR9gwygVK2",
    "GF7XD9": "dYuZAcGqWQYjtGPTSvacWY",
    "G98E3P": "34s6TgxQTWwsAQaqwHBv3U",
    "QRSQ8D": "bSaUBU9X5nBeMp7pWdNAGW",
    "3TTRKG": "wkefNPHyR4V115D8jvMNDC",
    "QQJ3ZS": "vQAunDod7FvMSD348rtxrv",
    "N3U3BT": "1JY5GBWLpe12bs1fGXMLgp",
    "PX7EHX": "kxzaXbKKtnRNH23XvpAZSN",
    "MKKVHX": "hyidpah6wPo91gz4tQW8YZ",
    "7AJEKD": "6QcpPoV5toTVi9dtHzR2TT",
    "HU8NSN": "qKNiW52zgX9tXGBFrBUwK8",
    "Y9AAMG": "xyiEgWGSUZVERTDcg2HqbB",
    "URWXGR": "9cExMatGbi3xH4hjJgndvt",
    "ENHZCR": "dEYt3WxM5V4jBk6BhT5oab",
    "GMUXZZ": "7N9bhdSHYq6zvfrt5E8mwN",
    "8HSWJD": "cBxLoU5N9g23C7QbBFsAf6",

    "ZXGJYA": "pJ1C6vLGhcJSfw5ZHvc6YA",
    "YE9MYB": "s8kxkasrJr38x4CiZcfSu6",
    "R393MD": "a4QnuwVmcDrEnjghxHspYt",
    "EDHADW": "55yLTdxSPh4ntJZRr5Gf1Q",
    "TPFDWN": "faxC1Tc6ukrDD7yZUZXaPw",
    "3LRN3P": "pj39SJYfUX9ZVXB6KHoGo7",
    "JSPF8U": "gbUPYbQSEmpFTn3hgYfuMN",
    "UKTQD8": "mmKVHh4uP9dvXCuUX7sKmo",
    "QCGUJB": "8EXSSxhAwwCyRtRGardF1e",
    "KDWXFH": "1Xed35oAQsDbPafBosMK1W",
    "3DBQCM": "nK3Hyq8hG1MtQ7zFdSQVpD",
    "97RZGZ": "tFZqwSVPX6nqeXvJedgzsG",
    "XGPBTU": "bRyRoC82NLkVtoiC58oj17",
}
recording_ids_drafts = {
    "H7YHTG": "uo31Qr3gSdd4zFh2knTpr5",
    # "PYQY3A": "monter-une-infrastructure-matomo",
    "EMG79M": "dQsWaFHLCAqnDhMyW34jDW",
    "MWQUT7": "qVqqbK6ezsJnZcbLg2HzPp",
    # "S37GBU": "gestion-de-projet-web-analytics",
    # "PU7SJR": "contributing-back",
    "33QBWR": "mR4XH2d6pJc1PUSokvgGBp",
    # "AXGTWL": "analysez-vos-performances",
    # "SXLAJL": "matomo-in-a-data-stack",
    # "SNEUXP": "migration-de-vos-datas-ga-vers-matomo",
    # "ADJLAW": "dashboards-with-apache-superset",
    # "PYT37H": "matomo-et-wordpress",
    # "QB8VY8": "using-kubernetes-and-docker",
    # "XMGR83": "les-traductions-dans-matomo",
    # "CQ3TRP": "vanilla-analytics",
    "U9GDMC": "kazVeZ6x7Tv13CZuJDQwa1",
    "SRDLAJ": "dFUE4UsdsAxmCtWLsMVdfS",
    # "XRVPDS": "das-problem-zu-wenig",
    # "7YDHL7": "tracking-spas",
    "FXLH93": "jjuoDmucxfLWTtzyfsn21a",
    "FUD7JR": "cyVg7Z1RJoDJdEJ5o81k65",
    "BRH8SH": "jbQpLLk2q7MEXqAggbinLA",
    "N3WJCA": "q2ij3WGyehmkpxxjSqguy1",
    # "389UYH": "joomla",
    "E893JM": "5opi9rRkxYLv9Fz2VWUAgA",
    "WXXXXE": "iWBWDy8DeF3RBSbVZkEnYs",
    "ST38HK": "jjzQEvcuw5fgsqmjD4d94J",

}
recording_ids_drafts = {**recording_ids_drafts, **recording_ids}

slides = {
    "GDGZXF": "https://schedule.matomocamp.org/media/matomocamp-2021/submissions/GDGZXF/resources/MatomoCamp_opening_ceremony_v2_ln8dBhV.pdf"
}

for name in chat_rooms.values():
    for letter in name:
        assert letter in set(ascii_lowercase).union(set(digits)).union({"-"})
