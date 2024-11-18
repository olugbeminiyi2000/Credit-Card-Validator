```javascript
function describePerson(person) {
  const descriptionParts = [
    'Name: ', person.name,
    ', Age: ', person.age,
    ', Hobbies: ', person.hobbies.join(', ')
  ];
  return descriptionParts.join('');
}
```
