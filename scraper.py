{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "response = requests.get(\"https://www.vox.com\")\n",
    "doc= BeautifulSoup(response.text)\n",
    "titles = doc.select('.c-newspaper_main')\n",
    "titles\n",
    "for title in titles:\n",
    "    print(title.text.strip())\n",
    "    print(title['href'])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.7 ('base')",
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
   "version": "3.9.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "e3411d863be6f7050f303885ae22dde21fa581b5bb4624b11ae48094fc2293e5"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
