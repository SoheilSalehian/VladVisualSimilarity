// ***********************************************************************
// GENERATED FILE -- DO NOT EDIT Unless custom instrumentation is required
// Parameterized with:
//
// EndpointName = index
// RequestName = dataPath
// RequestType = string
// ResponseName = status
// ResponseType = string
// ***********************************************************************

package main

import (
	"fmt"
	"time"

	"github.com/go-kit/kit/metrics"
)

type instrumentationMiddleware struct {
	requestCount   metrics.Counter
	requestLatency metrics.TimeHistogram
  // Add custom instrumentation 
  //
  //
  indexService
}

func (mw instrumentationMiddleware) index(dataPath string) (output string, err error) {
	defer func(begin time.Time) {
  methodField := metrics.Field{Key: "method", Value: "index"}
		errorField := metrics.Field{Key: "err", Value: fmt.Sprintf("%v", err)}
		mw.requestCount.With(methodField).With(errorField).Add(1)
		mw.requestLatency.With(methodField).With(errorField).Observe(time.Since(begin))
    // Add in observation calls for the custom instrumentation
    //
    //
	}(time.Now())

  output, err = mw.indexService.Callindex(dataPath)
	if err != nil {
   
    return "", err
  
	}

	return output, nil
}

