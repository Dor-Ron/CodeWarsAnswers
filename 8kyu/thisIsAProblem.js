function NameMe(first, last) {
    this.firstName = first;
    this.lastName = last;
    this.name = this.firstName + ' ' + this.lastName; // use this instead of 'return {name: this.firstName + ' ' + this.lastName}'
}
