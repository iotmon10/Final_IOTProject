double macase(int nrep, volatile float *dum)
/*
 *  Performs nrep loop its and returns mflops performed
 */
{
   register float m0, a0=0.0;
   register int i;
    m0=dum[0];
   for (i=0; i < nrep; i++)
   {
/*
 * Basic block 0
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 1
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 2
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 3
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 4
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 5
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 6
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 7
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 8
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 9
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 10
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 11
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 12
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 13
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 14
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 15
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 16
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 17
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 18
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 19
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 20
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 21
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 22
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 23
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 24
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 25
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 26
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 27
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 28
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 29
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 30
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 31
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 32
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 33
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 34
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 35
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 36
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 37
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 38
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 39
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 40
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 41
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 42
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 43
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 44
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 45
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 46
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 47
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 48
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 49
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 50
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 51
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 52
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 53
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 54
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 55
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 56
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 57
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 58
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 59
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 60
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 61
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 62
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 63
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 64
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 65
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 66
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 67
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 68
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 69
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 70
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 71
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 72
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 73
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 74
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 75
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 76
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 77
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 78
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 79
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 80
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 81
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 82
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 83
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 84
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 85
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 86
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 87
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 88
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 89
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 90
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 91
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 92
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 93
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 94
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 95
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 96
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 97
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 98
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 99
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 100
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 101
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 102
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 103
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 104
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 105
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 106
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 107
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 108
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 109
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 110
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 111
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 112
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 113
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 114
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 115
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 116
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 117
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 118
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 119
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 120
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 121
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 122
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 123
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 124
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 125
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 126
 */
      a0 += m0*m0;  m0=m0;
/*
 * Basic block 127
 */
      a0 += m0*m0;  m0=m0;
   }

   dum[0] = a0;
   return(nrep*256.0);
}
