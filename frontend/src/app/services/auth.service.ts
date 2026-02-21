import { Injectable, inject, PLATFORM_ID } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { isPlatformBrowser } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private http = inject(HttpClient);
  private platformId = inject(PLATFORM_ID);
  private apiUrl = 'http://192.168.60.1:8000';
  private tokenKey = 'tnecl_token';

  register(user: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, user);
  }

  verifyOtp(data: { email: string; otp: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/verify-otp`, data);
  }

  resendOtp(data: { email: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/resend-otp`, data);
  }

  loginRequest(data: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login-request`, data);
  }

  loginVerify(data: { email: string; otp: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login-verify`, data).pipe(
      tap((response: any) => {
        if (response.access_token && isPlatformBrowser(this.platformId)) {
          localStorage.setItem(this.tokenKey, response.access_token);
        }
      })
    );
  }

  login(credentials: FormData): Observable<any> {
    return this.http.post(`${this.apiUrl}/token`, credentials).pipe(
      tap((response: any) => {
        if (response.access_token && isPlatformBrowser(this.platformId)) {
          localStorage.setItem(this.tokenKey, response.access_token);
        }
      })
    );
  }

  logout(): void {
    if (isPlatformBrowser(this.platformId)) {
      localStorage.removeItem(this.tokenKey);
    }
  }

  isLoggedIn(): boolean {
    if (isPlatformBrowser(this.platformId)) {
      return !!localStorage.getItem(this.tokenKey);
    }
    return false;
  }

  getToken(): string | null {
    if (isPlatformBrowser(this.platformId)) {
      return localStorage.getItem(this.tokenKey);
    }
    return null;
  }
}
