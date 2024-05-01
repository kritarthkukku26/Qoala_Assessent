const assert = require('assert');
const http = require('http');

describe('Sample Application', function() {
  it('should return "Hello, world!"', function(done) {
    http.get('http://localhost:3000', function(res) {
      let data = '';

      res.on('data', function(chunk) {
        data += chunk;
      });

      res.on('end', function() {
        assert.strictEqual(data, 'Hello, world!\n');
        done();
      });
    });
  });
});
