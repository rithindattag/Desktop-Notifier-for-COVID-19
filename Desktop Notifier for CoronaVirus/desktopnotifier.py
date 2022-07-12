{
 "metadata": {
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
   "version": "3.9.5"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python395jvsc74a57bd0ac59ebe37160ed0dfa835113d9b8498d9f09ceb179beaac4002f036b9467c963",
   "display_name": "Python 3.9.5 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "ac59ebe37160ed0dfa835113d9b8498d9f09ceb179beaac4002f036b9467c963"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Desktop Notifier for COVID-19\n",
    "from urllib.request import urlopen, Request\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from win10toast import ToastNotifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "header = {\"User-Agent\": \"Mozilla\"}\n",
    "req = Request(\"https://www.worldometers.info/coronavirus/country/india/\", headers=header)\n",
    "html = urlopen(req)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<http.client.HTTPResponse at 0x280beacf850>"
      ]
     },
     "metadata": {},
     "execution_count": 5
    }
   ],
   "source": [
    "html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "metadata": {},
     "execution_count": 6
    }
   ],
   "source": [
    "html.status"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "obj = bs(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_cases = obj.find(\"li\", {\"class\":\"news_li\"}).strong.text.split()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "death = list(obj.find(\"li\", {\"class\":\"news_li\"}).strong.next_siblings)[1].text.split()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Notifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "notifier = ToastNotifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "message = \"New Cases - \"+ new_cases+\"\\nDeath - \"+death"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'New Cases - 4,221\\nDeath - 17'"
      ]
     },
     "metadata": {},
     "execution_count": 13
    }
   ],
   "source": [
    "message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "metadata": {},
     "execution_count": 15
    }
   ],
   "source": [
    "notifier.show_toast(title=\"COVID-19 Update\", msg=message, duration=5,)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}