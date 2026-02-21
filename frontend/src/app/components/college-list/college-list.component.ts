import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CollegeService, College } from '../../services/college.service';

@Component({
    selector: 'app-college-list',
    standalone: true,
    imports: [CommonModule, FormsModule, RouterLink],
    templateUrl: './college-list.component.html',
    styles: []
})
export class CollegeListComponent implements OnInit {
    colleges: College[] = [];
    filteredColleges: College[] = [];
    searchTerm = '';
    filterType = '';
    isLoading = true;
    private collegeService = inject(CollegeService);

    ngOnInit(): void {
        this.isLoading = true;
        this.collegeService.getColleges().subscribe({
            next: (data) => {
                console.log('Colleges loaded:', data.length);
                this.colleges = data;
                this.filteredColleges = data;
                this.isLoading = false;
            },
            error: (err) => {
                console.error('Error fetching colleges:', err);
                console.error('Error details:', err.message, err.status);
                this.isLoading = false;
            }
        });
    }

    applyFilters() {
        const term = this.searchTerm.toLowerCase().trim();
        this.filteredColleges = this.colleges.filter(c => {
            const matchesSearch = !term ||
                (c.name?.toLowerCase().includes(term)) ||
                (c.location?.toLowerCase().includes(term)) ||
                (c.code?.toLowerCase().includes(term));

            const matchesType = this.filterType === '' || c.type === this.filterType;
            return matchesSearch && matchesType;
        });
    }
}
