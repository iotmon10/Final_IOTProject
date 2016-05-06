#ifndef ATL_RESTRICT
#if defined(__STDC_VERSION__) && (__STDC_VERSION__/100 >= 1999)
   #define ATL_RESTRICT restrict
#else
   #define ATL_RESTRICT
#endif
#endif
void ATL_sJIK64x64x64TN64x64x0_a1_b1
   (const int M, const int N, const int K, const float alpha, const float * ATL_RESTRICT A, const int lda, const float * ATL_RESTRICT B, const int ldb, const float beta, float * ATL_RESTRICT C, const int ldc)
/*
 * matmul with TA=T, TB=N, MB=64, NB=64, KB=64, 
 * lda=64, ldb=64, ldc=0, mu=4, nu=4, ku=1, pf=0
 * Generated by ATLAS/tune/blas/gemm/emit_mm.c (3.10.2)
 */
{
   const float *stM = A + 4096;
   const float *stN = B + 4096;
   #define incAk 1
   const int incAm = 192, incAn = -4096;
   #define incBk 1
   const int incBm = -64, incBn = 256;
   #define incCm 4
   const int incCn = (((ldc) << 2)) - 64;
   float *pC0=C, *pC1=pC0+(ldc), *pC2=pC1+(ldc), *pC3=pC2+(ldc);
   const float *pA0=A;
   const float *pB0=B;
   register int k;
   register float rA0, rA1, rA2, rA3;
   register float rB0, rB1, rB2, rB3;
   register float rC0_0, rC1_0, rC2_0, rC3_0, rC0_1, rC1_1, rC2_1, rC3_1, rC0_2, rC1_2, rC2_2, rC3_2, rC0_3, rC1_3, rC2_3, rC3_3;
   do /* N-loop */
   {
      do /* M-loop */
      {
/*
 *       Peel 1st iter to assign C regs
 */
         rA0 = *pA0;
         rB0 = *pB0;
         rA1 = pA0[64];
         rA2 = pA0[128];
         rA3 = pA0[192];
         rB1 = pB0[64];
         rB2 = pB0[128];
         rB3 = pB0[192];
         rC0_0 = rA0 * rB0;
         rC1_0 = rA1 * rB0;
         rC2_0 = rA2 * rB0;
         rC3_0 = rA3 * rB0;
         rC0_1 = rA0 * rB1;
         rC1_1 = rA1 * rB1;
         rC2_1 = rA2 * rB1;
         rC3_1 = rA3 * rB1;
         rC0_2 = rA0 * rB2;
         rC1_2 = rA1 * rB2;
         rC2_2 = rA2 * rB2;
         rC3_2 = rA3 * rB2;
         rC0_3 = rA0 * rB3;
         rC1_3 = rA1 * rB3;
         rC2_3 = rA2 * rB3;
         rC3_3 = rA3 * rB3;
         pA0 += incAk;
         pB0 += incBk;
/*
 *       Unpeeled K iterations
 */
         for (k=0; k < 63; k++) /* easy loop to unroll */
         {
            rA0 = *pA0;
            rB0 = *pB0;
            rA1 = pA0[64];
            rA2 = pA0[128];
            rA3 = pA0[192];
            rB1 = pB0[64];
            rB2 = pB0[128];
            rB3 = pB0[192];
            rC0_0 += rA0 * rB0;
            rC1_0 += rA1 * rB0;
            rC2_0 += rA2 * rB0;
            rC3_0 += rA3 * rB0;
            rC0_1 += rA0 * rB1;
            rC1_1 += rA1 * rB1;
            rC2_1 += rA2 * rB1;
            rC3_1 += rA3 * rB1;
            rC0_2 += rA0 * rB2;
            rC1_2 += rA1 * rB2;
            rC2_2 += rA2 * rB2;
            rC3_2 += rA3 * rB2;
            rC0_3 += rA0 * rB3;
            rC1_3 += rA1 * rB3;
            rC2_3 += rA2 * rB3;
            rC3_3 += rA3 * rB3;
            pA0 += incAk;
            pB0 += incBk;
         }
         *pC0 += rC0_0;
         pC0[1] += rC1_0;
         pC0[2] += rC2_0;
         pC0[3] += rC3_0;
         *pC1 += rC0_1;
         pC1[1] += rC1_1;
         pC1[2] += rC2_1;
         pC1[3] += rC3_1;
         *pC2 += rC0_2;
         pC2[1] += rC1_2;
         pC2[2] += rC2_2;
         pC2[3] += rC3_2;
         *pC3 += rC0_3;
         pC3[1] += rC1_3;
         pC3[2] += rC2_3;
         pC3[3] += rC3_3;
         pC0 += incCm;
         pC1 += incCm;
         pC2 += incCm;
         pC3 += incCm;
         pA0 += incAm;
         pB0 += incBm;
      }
      while(pA0 != stM);
      pC0 += incCn;
      pC1 += incCn;
      pC2 += incCn;
      pC3 += incCn;
      pA0 += incAn;
      pB0 += incBn;
   }
   while(pB0 != stN);
}
#ifdef incAm
   #undef incAm
#endif
#ifdef incAn
   #undef incAn
#endif
#ifdef incAk
   #undef incAk
#endif
#ifdef incBm
   #undef incBm
#endif
#ifdef incBn
   #undef incBn
#endif
#ifdef incBk
   #undef incBk
#endif
#ifdef incCm
   #undef incCm
#endif
#ifdef incCn
   #undef incCn
#endif
#ifdef incCk
   #undef incCk
#endif
#ifdef Mb
   #undef Mb
#endif
#ifdef Nb
   #undef Nb
#endif
#ifdef Kb
   #undef Kb
#endif