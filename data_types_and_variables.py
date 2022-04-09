{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8f268314",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(99.9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3e54e121",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(\"False\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8a8e6d5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c00acb8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type('0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cf6090bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "630d5f42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5bf8af42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type('True')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d7569833",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type([{}])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b873238d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type({'a': []})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d1301198",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/3101731670.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m'1'\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "'1' + 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "eb076b23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "6 % 4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "660db550",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(6 % 4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9ee0912b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(type(6 % 4))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b3b7b6a5",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/2745667065.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m'3 + 4 is '\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m3\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "'3 + 4 is ' + 3 + 4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5a36a2e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0 < 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "de871dd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'False' == False\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9cef706b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True == 'True'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f5f8896f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 >= -5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "70d82f85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True or \"42\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "bb14deb7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "6 % 5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a1d74768",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 < 4 and 1 == 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f7cfb012",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'codeup' == 'codeup' and 'codeup' == 'Codeup'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5940d714",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3850088429.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/3850088429.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    4 >= 0 and 1 !== '1'\u001b[0m\n\u001b[0m                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "4 >= 0 and 1 !== '1'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b23e6995",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "6 % 3 == 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "70f48344",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 % 2 != 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "df056b49",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate list (not \"int\") to list",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/690870975.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate list (not \"int\") to list"
     ]
    }
   ],
   "source": [
    "[1] + 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3b862cb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[1] + [2]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0ac9e04f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 1]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[1] * 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "0d9947ae",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can't multiply sequence by non-int of type 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/3987011808.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can't multiply sequence by non-int of type 'list'"
     ]
    }
   ],
   "source": [
    "[1] * [2]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "f10fa027",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[] + [] == []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "567fe0c7",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'dict' and 'dict'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/1120052685.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'dict' and 'dict'"
     ]
    }
   ],
   "source": [
    "{} + {}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ac0c05d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "35d210e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "The_Little_Mermaid = 3\n",
    "Brother_Bear = 5\n",
    "Hercules = 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ce22bc80",
   "metadata": {},
   "outputs": [],
   "source": [
    "Movies = [The_Little_Mermaid, Brother_Bear, Hercules]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e48697b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 1]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "c7fdf99b",
   "metadata": {},
   "outputs": [],
   "source": [
    "Rental_price = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "bd32afbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Rental_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "4da26a59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 1, 3, 5, 1, 3, 5, 1]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Movies * Rental_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8f35be87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 1, 3, 5, 1, 3, 5, 1]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for m in Movies:\n",
    "    movie_rental = Movies * Rental_price\n",
    "movie_rental"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "5fffbc02",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can't multiply sequence by non-int of type 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/3035826935.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mm\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mMovies\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0mRental_price\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mRental_price\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0mMovies\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mRental_price\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: can't multiply sequence by non-int of type 'list'"
     ]
    }
   ],
   "source": [
    "for m in Movies:\n",
    "    Rental_price = Rental_price * Movies\n",
    "Rental_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b0f0154d",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can't multiply sequence by non-int of type 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22381/2780423951.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mm\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mMovies\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0mMovies\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mMovies\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0mRental_price\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mMovies\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: can't multiply sequence by non-int of type 'list'"
     ]
    }
   ],
   "source": [
    "for m in Movies:\n",
    "    Movies = Movies * Rental_price\n",
    "Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "21fa3f06",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 1, 3, 5, 1, 3, 5, 1]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Rental_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "ff4fb09f",
   "metadata": {},
   "outputs": [],
   "source": [
    "Rental_price = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "51432f3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 1]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4d6ae39",
   "metadata": {},
   "outputs": [],
   "source": [
    "for m in Movies:\n",
    "    Movies = Movies * Rental_price\n",
    "Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e55be6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02f5c521",
   "metadata": {},
   "outputs": [],
   "source": [
    "list(Movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2446f01b",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(Movies):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cc25d08",
   "metadata": {},
   "outputs": [],
   "source": [
    "Test = 123"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f4193e9d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Test' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22806/579046729.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mTest\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'Test' is not defined"
     ]
    }
   ],
   "source": [
    "Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e072f92c",
   "metadata": {},
   "outputs": [],
   "source": [
    "The_Little_Mermaid = 3\n",
    "Brother_Bear = 5\n",
    "Hercules = 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f447ce33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 1]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Movies = [The_Little_Mermaid, Brother_Bear, Hercules]\n",
    "Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "bccb29d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rental = 3\n",
    "rental"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e4422f75",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22806/261602887.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0mx\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0mrental\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mMovies\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "[x * rental for x in Movies()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "67db8be1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[380, 350, 400]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Amazon = 380\n",
    "Facebook = 350\n",
    "Google = 400\n",
    "\n",
    "Com = [Amazon, Facebook, Google]\n",
    "Com\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "df0dcdbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 6, 4]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "w_fb = 10\n",
    "w_goog = 6\n",
    "w_amz = 4\n",
    "\n",
    "w_hrs = [w_fb, w_goog, w_amz]\n",
    "w_hrs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a2ec1404",
   "metadata": {},
   "outputs": [],
   "source": [
    "class_sizes = [24, 26, 29, 22, 25, 18, 24]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b35175c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class_schedule = range(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7ec925bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[24, 26, 29, 22, 25, 18, 24]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class_sizes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c2169dc8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 7)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class_schedule"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4f8d63a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(class_schedule)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "da129618",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[True, True, False, True, True, True, True]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[max <= 27 for max in class_sizes]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "47d84620",
   "metadata": {},
   "outputs": [],
   "source": [
    "rentals = [3, 5, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7a18c413",
   "metadata": {},
   "outputs": [],
   "source": [
    "rental_total = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ef5b0127",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +=: 'int' and 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22806/3686403983.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mrental_total\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mrentals\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +=: 'int' and 'list'"
     ]
    }
   ],
   "source": [
    "rental_total += [rentals * 3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89e3d2dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "class_full = False\n",
    "class_schedule_conflict = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e9815656",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3950479053.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22806/3950479053.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    can_be_enrolled = Not class_full\u001b[0m\n\u001b[0m                          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "can_be_enrolled = Not class_full"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ed7eedda",
   "metadata": {},
   "outputs": [],
   "source": [
    "is_premium = True #or False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "66bc110a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'product_offer' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/tg/c6tcjwk13mj583lxrf25k3jm0000gn/T/ipykernel_22806/236421841.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0moffer_expired\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m \u001b[0;31m#or True\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mno_items\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mproduct_offer\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;32mnot\u001b[0m \u001b[0moffer_expired\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mno_items\u001b[0m \u001b[0;34m>\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mis_premium\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mproduct_offer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'product_offer' is not defined"
     ]
    }
   ],
   "source": [
    "offer_expired = False #or True\n",
    "no_items = 3\n",
    "product_offer - (not offer_expired and no_items >2) or is_premium\n",
    "print(product_offer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f4a457b",
   "metadata": {},
   "outputs": [],
   "source": [
    "five_character_or_more = len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "176ad117",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = -5\n",
    "\n",
    "r = x % 2\n",
    "r"
   ]
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
