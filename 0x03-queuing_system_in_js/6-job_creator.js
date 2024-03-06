import kue from 'kue'
const queue = kue.createQueue()
const data = {phoneNumber: '123456', message: 'hello'}
let job = queue.create('push_notification', data);
job.on('enqueue', () => {
	  console.log('Notification job created:', job.id);
	    })
  .on('complete', () => {
	      console.log('Notification job completed');
	    })
  .on('failed attempt', () => {
	      console.log('Notification job failed');
	    });
job.save();
