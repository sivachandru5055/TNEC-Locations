import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
    selector: 'app-register',
    standalone: true,
    imports: [CommonModule, FormsModule, RouterLink],
    templateUrl: './register.component.html',
    styles: []
})
export class RegisterComponent {
    // Registration form
    name = '';
    email = '';
    password = '';

    // OTP verification
    showOtpForm = false;
    otp = '';
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

        this.authService.register({
            email: this.email,
            password: this.password,
            name: this.name
        }).subscribe({
            next: (res) => {
                this.isLoading = false;
                if (res.verified) {
                    // Auto-verified (SMTP not configured) - go straight to login
                    this.message = res.message || 'Registration successful!';
                    alert(this.message + ' Redirecting to login...');
                    this.router.navigate(['/login']);
                } else {
                    // OTP sent - show verification form
                    this.showOtpForm = true;
                    this.message = res.message || 'OTP sent to your email!';
                    this.startResendCooldown();
                }
            },
            error: (err) => {
                this.isLoading = false;
                this.errorMessage = err.error?.detail || 'Registration failed.';
            }
        });
    }

    onVerifyOtp(event: Event) {
        event.preventDefault();
        this.isLoading = true;
        this.errorMessage = '';

        this.authService.verifyOtp({ email: this.email, otp: this.otp }).subscribe({
            next: (res) => {
                this.isLoading = false;
                this.message = res.message || 'Email verified!';
                setTimeout(() => this.router.navigate(['/login']), 1500);
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

        this.authService.resendOtp({ email: this.email }).subscribe({
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
            if (this.resendCooldown <= 0) {
                clearInterval(this.cooldownInterval);
            }
        }, 1000);
    }

    ngOnDestroy() {
        if (this.cooldownInterval) clearInterval(this.cooldownInterval);
    }
}
