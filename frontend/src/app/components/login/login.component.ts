import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [CommonModule, FormsModule, RouterLink],
    templateUrl: './login.component.html',
    styles: []
})
export class LoginComponent {
    email = '';
    password = '';
    otp = '';
    showOtpForm = false;
    message = '';
    errorMessage = '';
    isLoading = false;
    resendCooldown = 0;

    private authService = inject(AuthService);
    private router = inject(Router);
    private cooldownInterval: any;

    onSubmit(event: Event) {
        event.preventDefault();
        this.isLoading = true;
        this.errorMessage = '';

        this.authService.loginRequest({ email: this.email, password: this.password }).subscribe({
            next: (res) => {
                this.isLoading = false;
                this.showOtpForm = true;
                this.message = res.message || 'OTP sent to your email!';
                this.startResendCooldown();
            },
            error: (err) => {
                this.isLoading = false;
                this.errorMessage = err.error?.detail || 'Login failed.';
            }
        });
    }

    onVerifyOtp(event: Event) {
        event.preventDefault();
        this.isLoading = true;
        this.errorMessage = '';

        this.authService.loginVerify({ email: this.email, otp: this.otp }).subscribe({
            next: () => {
                this.isLoading = false;
                this.router.navigate(['/dashboard']);
            },
            error: (err) => {
                this.isLoading = false;
                this.errorMessage = err.error?.detail || 'OTP verification failed.';
            }
        });
    }

    onResendOtp() {
        if (this.resendCooldown > 0) return;
        this.isLoading = true;
        this.errorMessage = '';

        this.authService.loginRequest({ email: this.email, password: this.password }).subscribe({
            next: (res) => {
                this.isLoading = false;
                this.message = res.message || 'New OTP sent!';
                this.startResendCooldown();
            },
            error: (err) => {
                this.isLoading = false;
                this.errorMessage = err.error?.detail || 'Failed to resend OTP.';
            }
        });
    }

    private startResendCooldown() {
        this.resendCooldown = 30;
        if (this.cooldownInterval) clearInterval(this.cooldownInterval);
        this.cooldownInterval = setInterval(() => {
            this.resendCooldown--;
            if (this.resendCooldown <= 0) clearInterval(this.cooldownInterval);
        }, 1000);
    }

    ngOnDestroy() {
        if (this.cooldownInterval) clearInterval(this.cooldownInterval);
    }
}
