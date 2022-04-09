{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be6f6cc5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a day of the week. Sunday\n",
      "It's not Monday\n"
     ]
    }
   ],
   "source": [
    "#1. Conditional Basics\n",
    "    #1a. prompt the user for a day of the week, print out whether the day is Monday or not\n",
    "    \n",
    "if input(\"Enter a day of the week. \") == 'Monday':\n",
    "    print('It\\'s Monday')\n",
    "else:\n",
    "    print('It\\'s not Monday')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "932a371c",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (1455843229.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_24667/1455843229.py\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    print('It\\'s a weekday')\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "    #1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend\n",
    "    \n",
    "if input(\"Enter a day of the week. \") == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':\n",
    "    print('It\\'s a weekday')\n",
    "else:\n",
    "    print('It\\'s a weekend')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb22f18d",
   "metadata": {},
   "outputs": [],
   "source": [
    "if input(\"Enter a day of the week. \") == 'Monday':\n",
    "    print('It\\'s a weekday')\n",
    "elif input(\"Enter a day of the week. \") == 'Tuesday':\n",
    "    print('It\\'s a weekday')\n",
    "elif input(\"Enter a day of the week. \") == 'Wednesday':\n",
    "    print('It\\'s a weekday')\n",
    "elif input(\"Enter a day of the week. \") == 'Thursday':\n",
    "    print('It\\'s a weekday')\n",
    "elif input(\"Enter a day of the week. \") == 'Friday':\n",
    "    print('It\\'s a weekday')\n",
    "elif input(\"Enter a day of the week. \") == 'Saturday':\n",
    "    print('It\\'s a weekend')\n",
    "elif input(\"Enter a day of the week. \") == 'Sunday':\n",
    "    print('It\\'s a weekend')\n",
    "else :\n",
    "    print('Try again')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ed5d006b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[18, 33, 42, 57, 64, 86]\n",
      "15\n",
      "[270, 495, 630, 855, 960, 1290]\n",
      "[-22, -7, 2, 17, 24, 46]\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_24869/2619844487.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     23\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mOvertime\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 25\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mOvertime\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     26\u001b[0m         \u001b[0mWage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mRate\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mRate\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m.5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "#c. create variables and make up values for\n",
    "        #• the number of hours worked in one week\n",
    "        #• the hourly rate\n",
    "        #• how much the week's paycheck will be\n",
    "        #• write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours\n",
    "        \n",
    "#Time = time in hours\n",
    "Time = [18, 33, 42, 57, 64, 86]\n",
    "print(Time)\n",
    "\n",
    "#Rate = hourly rate\n",
    "Rate = 15\n",
    "print(Rate)\n",
    "\n",
    "#Wage = the week's paycheck\n",
    "\n",
    "Wage = [x * Rate for x in Time]\n",
    "print(Wage)\n",
    "\n",
    "#Overtime = paid time and a half\n",
    "Overtime = [x - 40 for x in Time]\n",
    "print(Overtime)\n",
    "\n",
    "for x in Overtime:\n",
    "    if Overtime[x] > 0:\n",
    "        Wage = Rate + (Rate * .5)\n",
    "else:\n",
    "    Wage = [x * Rate for x in Time]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e3ac1efa",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'>' not supported between instances of 'list' and 'int'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_24869/4153053283.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mO\u001b[0m \u001b[0;34m>\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mnone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: '>' not supported between instances of 'list' and 'int'"
     ]
    }
   ],
   "source": [
    "for x in Overtime:\n",
    "    if Overtime[x] > 0:\n",
    "    Wage = Rate + (Rate * .5)\n",
    "else:\n",
    "    Wage = [x * Rate for x in Time]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b873f37c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b3a603b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
