{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a43903f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fetching HDFC Top 100\n",
      "Saved 125497_nav.csv\n",
      "Fetching SBI Bluechip\n",
      "Saved 119551_nav.csv\n",
      "Fetching ICICI Bluechip\n",
      "Saved 120503_nav.csv\n",
      "Fetching Nippon Large Cap\n",
      "Saved 118632_nav.csv\n",
      "Fetching Axis Bluechip\n",
      "Saved 119092_nav.csv\n",
      "Fetching Kotak Bluechip\n",
      "Saved 120841_nav.csv\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "SAVE_PATH = r\"D:\\projects\\mutual-fund-analytics\\data\\raw\"\n",
    "\n",
    "def fetch_nav(scheme_code):\n",
    "\n",
    "    url = f\"https://api.mfapi.in/mf/{scheme_code}\"\n",
    "\n",
    "    response = requests.get(url)\n",
    "\n",
    "    if response.status_code != 200:\n",
    "        print(f\"Failed for {scheme_code}\")\n",
    "        return\n",
    "\n",
    "    data = response.json()\n",
    "\n",
    "    df = pd.DataFrame(data[\"data\"])\n",
    "\n",
    "    file_name = f\"{scheme_code}_nav.csv\"\n",
    "\n",
    "    df.to_csv(\n",
    "        os.path.join(SAVE_PATH, file_name),\n",
    "        index=False\n",
    "    )\n",
    "\n",
    "    print(f\"Saved {file_name}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    schemes = {\n",
    "        \"HDFC Top 100\": 125497,\n",
    "        \"SBI Bluechip\": 119551,\n",
    "        \"ICICI Bluechip\": 120503,\n",
    "        \"Nippon Large Cap\": 118632,\n",
    "        \"Axis Bluechip\": 119092,\n",
    "        \"Kotak Bluechip\": 120841\n",
    "    }\n",
    "\n",
    "    for name, code in schemes.items():\n",
    "        print(f\"Fetching {name}\")\n",
    "        fetch_nav(code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fbba31d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
